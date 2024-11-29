#!/usr/bin/python3
import sys
import os
import time
import json
import subprocess
import yaml
import Bitwarden
import VirtexBitwarden

from pick import pick
from colorama import Fore, Back, Style
import Keys
import glob



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
   
    # Specify the directory
    directory =  calc_ref_path()
    print(directory)
    # Use glob to find all files with the .bwref.yaml extension
    files = glob.glob(os.path.join(directory, '*.bwref.yaml'))
    print(directory)
    option,index = pick(files, title)
    return option,index

def pick_template():
    
    formats= ["Username","Password", "Password+[ENTER]", "Username+[TAB]+Password+[ENTER]"]
    templates = [{"name": "Username", "template": "{username}"},
        {"name": "Pasword", "template": "{password}\n"},
        {"name": "Username [tab] Password [enter]",
        "template": "{username}\t{password}\n"}
    ]
    option,index = pick(formats, "Output Format:")
    
    return templates[index]["template"]


def create_bwref(searchTerm):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    env =  Bitwarden.unlock_bitwarden()
    resultJson = subprocess.run(["/usr/local/bin/bw", "list", "items", "--search", searchTerm], capture_output=True, text=True, env=env).stdout
    items = json.loads(resultJson)  
    itemsFormatted = []
    for element in items:
        itemsFormatted.append({'id': element["id"], 'name': element["name"] })

    option, index = pick(itemsFormatted, "Select an item:")
    newRef = Bitwarden.create_ref(option["id"])
    print("Enter name: ")
    name = input()
    outPath = os.path.join( calc_ref_path(), f"{name}.bwref.yaml")
    with open(outPath, 'w') as file:
        yaml.dump(newRef, file)

def send_bitwarden_item():
    option,index = pick_item()
    env = Bitwarden.unlock_bitwarden()
    bwRefPath =  os.path.join(VirtexBitwarden.calc_ref_path(),  option)
    bwRef = load_bitwarden_ref(bwRefPath)
    template = pick_template()
    secret = Bitwarden.get_item(bwRef["id"], env)
    compiledString = replace_template_tokens(template, secret["login"]["username"], secret["login"]["password"])
    Keys.type_string(compiledString)