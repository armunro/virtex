#!/usr/bin/python3
import sys
import os
import time
import json
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from HID import CODE
import HID


def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def replace_template_tokens(template, username, password):
    return template.replace("{username}", username).replace("{password}", password)

def unlock_bitwarden():
    print("Unlocking Bitwarden")
    my_env = os.environ.copy()
    sessionId = subprocess.run(["/usr/local/bin/bw", "unlock", "--passwordfile=master.bwpass.txt", "--raw"], capture_output=True, text=True).stdout
    my_env["BW_SESSION"] = sessionId
    return my_env

def get_bitwarden_secret(itemId):
    envi = unlock_bitwarden()
    print("Getting " + itemId)
    resultJson = subprocess.run(["/usr/local/bin/bw", "get", "item", itemId], capture_output=True, text=True, env=envi).stdout
    secret = json.loads(resultJson)
    return secret

def load_bitwarden_ref(refPath):
    data = load_json(refPath)
    return data


if __name__ == "__main__":
    json_filename = sys.argv[1]
    bwRef = load_bitwarden_ref(json_filename)
    secret = get_bitwarden_secret(bwRef["id"])
    compiledString = replace_template_tokens(bwRef["template"], secret["login"]["username"], secret["login"]["password"])
    HID.type_string(compiledString)