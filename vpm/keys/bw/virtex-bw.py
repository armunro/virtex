#!/usr/bin/python3
import sys
import os
import time

import json
import subprocess

# Import the module from the parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from HID import CODE
import HID


def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def get_bitwarden_item_credentials(item_name):

   
    return secret

def replace_template_tokens(template, username, password):
    return template.replace("{username}", username).replace("{password}", password)


if __name__ == "__main__":
    json_filename = sys.argv[1]
     # Load the JSON file
    data = load_json(json_filename)
    
    # Get Bitwarden credentials (username, password) for the specified item name
    item_name = data['id']
    template = data['template']
    my_env = os.environ.copy()
    sessionId = subprocess.run(["/usr/local/bin/bw", "unlock", "--passwordfile=bw-password.txt", "--raw"], capture_output=True, text=True).stdout
    my_env["BW_SESSION"] = sessionId

    print("getting " + item_name)
    resultJson = subprocess.run(["/usr/local/bin/bw", "get", "item", item_name], capture_output=True, text=True, env=my_env).stdout
    secret = json.loads(resultJson)
    secret = get_bitwarden_item_credentials(item_name)
    
    # Replace tokens in the template with actual username and password
    filled_template = replace_template_tokens(template, secret["login"]["username"], secret["login"]["password"])
    
    # Output the final result (or process it further, like writing to HID device)
    HID.type_string(filled_template)

    
  
    