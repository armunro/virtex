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
from tqdm import tqdm

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

if __name__ == "__main__":
    with tqdm(total=4, desc="Processing", unit="step") as pbar:
        option,index = pick_item()
        pbar.update(1)
        env = Bitwarden.unlock_bitwarden()
        pbar.update(2)
        bwRefPath =  os.path.join(Bitwarden.calc_ref_path(),  option)
        bwRef = load_bitwarden_ref(bwRefPath)
        pbar.update(3)
        secret = Bitwarden.get_item(bwRef["id"], env)
        compiledString = replace_template_tokens(bwRef["template"], secret["login"]["username"], secret["login"]["password"])
        HID.type_string(compiledString)
        pbar.update(4)
        pbar.close()