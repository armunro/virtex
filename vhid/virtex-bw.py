#!/usr/bin/python3
import sys
import os
import time
import json
import subprocess
import yaml
import Bitwarden
from pick import pick
from colorama import Fore, Back, Style
from alive_progress import alive_bar

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from HID import CODE
import HID

def replace_template_tokens(template, username, password):
    return template.replace("{username}", username).replace("{password}", password)

def load_bitwarden_ref(refPath):
    with open(refPath, 'r') as file:
        data = yaml.safe_load(file)
        return data

def pick_item():
    title = 'Select Bitwarden Item: '
    path = Bitwarden.calc_ref_path()
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]  
    option,index = pick(files, title)
    return option,index

def pick_template():
    formats = [{"name": "Username", "template": "{username}"},
        {"name": "Pasword", "template": "{password}"},
        {"name": "Username [tab] Password [enter]",
        "template": "{username}\t{password}\n"}
    ]
    return pick(formats, "Output Format:")

if __name__ == "__main__":
    with alive_bar(7, manual=True) as bar:
        bar(.1)
        option,index = pick_item()
        bar(.2)
        env = Bitwarden.unlock_bitwarden()
        bar(.3)
        bwRefPath =  os.path.join(Bitwarden.calc_ref_path(),  option)
        bar(.4)
        bwRef = load_bitwarden_ref(bwRefPath)
        bar(.5)
        option,index = pick_template()
        bar(.6)
        secret = Bitwarden.get_item(bwRef["id"], env)
        compiledString = replace_template_tokens(option["template"], secret["login"]["username"], secret["login"]["password"])
        HID.type_string(compiledString)
        bar(.7)