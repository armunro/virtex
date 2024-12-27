import sys
import os
import time
import json
import subprocess
import yaml
import Bitwarden
from pick import pick
from colorama import Fore, Back, Style
import Keys
import glob
from dotenv import load_dotenv

def unlock_bitwarden():
    my_env = os.environ.copy()
    
    load_dotenv()
    if 'BW_SESSION' in os.environ:
            my_env["BW_SESSION"] = os.environ["BW_SESSION"]
    else:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        sessionId = subprocess.run(["/usr/local/bin/bw", "unlock", "--passwordfile=" + script_dir + "../../virtex-data/bitwarden/master.bwpass.txt", "--raw"], capture_output=True, text=True).stdout
        my_env["BW_SESSION"] = sessionId
        with open(".env", 'w') as file:
            file.write("BW_SESSION=" + sessionId)
    return my_env

def get_item(id, env):
    result = subprocess.run(["/usr/local/bin/bw", "get", "item", id], capture_output=True, text=True, env=env)
    item = json.loads(result.stdout)
    return item


def create_ref(id, template="{username}\t{password}\n"):
    return {'id': id, 'template': template}

def replace_template_tokens(template, username, password):
    return template.replace("{username}", username).replace("{password}", password)

def load_bitwarden_ref(refPath):
    with open(refPath, 'r') as file:
        data = yaml.safe_load(file)
        return data
def calc_ref_path():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(script_dir, "..","..","virtex-data", "bitwarden")
    return path

def pick_item():
    title = 'Select Bitwarden Item: '
    directory =  calc_ref_path()
    files = glob.glob(os.path.join(directory, '*.bwref.yaml'))
    option,index = pick(files, title)
    return option,index

def pick_template():
    formats= ["Username","Password", "Password+[ENTER]", "Username+[TAB]+Password+[ENTER]"]
    templates = ["{username}", "{password}", "{password}\n","{username}\t{password}\n"]
    option,index = pick(formats, "Output Format:")
    return templates[index]

def create_bwref(searchTerm):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    env =  unlock_bitwarden()
    resultJson = subprocess.run(["/usr/local/bin/bw", "list", "items", "--search", searchTerm], capture_output=True, text=True, env=env).stdout
    items = json.loads(resultJson)  
    itemsFormatted = []
    for element in items:
        itemsFormatted.append({'id': element["id"], 'name': element["name"] })

    option, index = pick(itemsFormatted, "Select an item:")
    newRef = create_ref(option["id"])
    print("Enter name: ")
    name = input()
    outPath = os.path.join( calc_ref_path(), f"{name}.bwref.yaml")
    with open(outPath, 'w') as file:
        yaml.dump(newRef, file)


def send_bitwarden_item():
    option,index = pick_item()
    env = unlock_bitwarden()
    bwRefPath =  os.path.join(calc_ref_path(),  option)
    bwRef = load_bitwarden_ref(bwRefPath)
    template = pick_template()
    secret = get_item(bwRef["id"], env)
    compiledString = replace_template_tokens(template, secret["login"]["username"], secret["login"]["password"])
    Keys.type_string(compiledString)
    
def send_bitwarden_item2(ref, template):
    env = unlock_bitwarden()
    bwRefPath =  os.path.join(calc_ref_path(),  ref)
    bwRef = load_bitwarden_ref(bwRefPath)
    secret = get_item(bwRef["id"], env)
    compiledString = replace_template_tokens(template, secret["login"]["username"], secret["login"]["password"])
    Keys.type_string(compiledString)
