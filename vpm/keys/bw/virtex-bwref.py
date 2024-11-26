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
from dotenv import load_dotenv



if __name__ == "__main__":
    term = sys.argv[1]
    with tqdm(total=4, desc="Processing", unit="step") as pbar:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        
        pbar.set_description("Unlock Bitwarden")
        pbar.update(1)
        env =  Bitwarden.unlock_bitwarden()

        pbar.update(2)
        pbar.set_description("Searching Bitwarden for '" + term + "'")
        resultJson = subprocess.run(["/usr/local/bin/bw", "list", "items", "--search", term], capture_output=True, text=True, env=env).stdout
        items = json.loads(resultJson)  
        
        pbar.update(3)
        itemsFormatted = []
        for element in items:
            itemsFormatted.append({'id': element["id"], 'name': element["name"] })

        option, index = pick(itemsFormatted, "Select an item:")
        newRef = create_ref(option["id"])
        print("Enter name: ")
        name = input()
        outPath = os.path.join(script_dir, 'refs/', name + '.bwref.yaml')
        with open(outPath, 'w') as file:
            yaml.dump(newRef, file)
        pbar.update(4)