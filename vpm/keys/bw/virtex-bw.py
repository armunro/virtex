#!/usr/bin/python3
import sys
import os
import time
import json
import subprocess
import yaml
from pick import pick
from colorama import Fore, Back, Style
from tqdm import tqdm
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from HID import CODE
import HID
def is_bitwarden_unlocked():
    try:
        result = subprocess.run(['/usr/local/bin/bw', 'status'], capture_output=True, text=True, check=True)
        status = json.loads(result.stdout)
        
        # Check if the status indicates that Bitwarden is unlocked
        return status.get('status') == 'unlocked'
    except subprocess.CalledProcessError as e:
        print(f"Error checking Bitwarden status: {e}")
        return False


def replace_template_tokens(template, username, password):
    return template.replace("{username}", username).replace("{password}", password)



def get_bitwarden_secret(itemId):
    with tqdm(total=4, desc="Processing", unit="step") as pbar:
        pbar.update(1)
        pbar.set_description("Unlocking Bitwarden")
        my_env = os.environ.copy()
        script_dir = os.path.dirname(os.path.realpath(__file__))
        load_dotenv()
        if 'BW_SESSION' in os.environ:
            my_env["BW_SESSION"] = os.environ["BW_SESSION"]
        else:
            pbar.update(2)
            sessionId = subprocess.run(["/usr/local/bin/bw", "unlock", "--passwordfile=" + script_dir + "/master.bwpass.txt", "--raw"], capture_output=True, text=True).stdout
            my_env["BW_SESSION"] = sessionId
            with open(".env", 'w') as file:
                file.write("BW_SESSION=" + sessionId)
        

        pbar.update(3)
        pbar.set_description("Getting " + itemId)
        resultJson = subprocess.run(["/usr/local/bin/bw", "get", "item", itemId], capture_output=True, text=True, env=my_env).stdout
        
        pbar.update(4)
        secret = json.loads(resultJson)
        
        return secret

def load_bitwarden_ref(refPath):
    with open(refPath, 'r') as file:
        data = yaml.safe_load(file)
        return data


if __name__ == "__main__":

    title = 'Select Bitwarden Item: '

    script_dir = os.path.dirname(os.path.realpath(__file__))

    path = script_dir + "/refs"

    # Get a list of all files in the 'refs' subdirectory
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]  
    option, index = pick(files, title)
    bwRefPath =  path + "/" + option
    bwRef = load_bitwarden_ref(bwRefPath)
    print(bwRefPath)
    secret = get_bitwarden_secret(bwRef["id"])
    compiledString = replace_template_tokens(bwRef["template"], secret["login"]["username"], secret["login"]["password"])
    HID.type_string(compiledString)