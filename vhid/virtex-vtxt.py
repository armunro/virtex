#!/usr/bin/python3
import sys
import os
import time
import json
import subprocess
import yaml
import Bitwarden
import re
from pick import pick
from colorama import Fore, Back, Style
from tqdm import tqdm
from dotenv import load_dotenv


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from HID import CODE
import HID
import HID.utils.windows

def parse_line(line):
    pattern = r'(\w+): (\w+)'
    matches = re.findall(pattern, line)
    for match in matches:
        command, value = match
        if (command.lower() == "print"):
            HID.type_string(value)
        if (command.lower() == "winrun"):
            HID.utils.windows.open_run()
        if (command.lower() == "winstart"):
            HID.utils.windows.open_start()
        if (command.lower() == "notepad"):
            HID.utils.windows.notepad()
        if (command.lower() == "sleep"):
            time.sleep(float(value))
        if (command.lower() == "enter"):
            HID.press(bytes([0, 0, HID.CODE.ENTER, *[0] * 5]))
        if (command.lower() == "key"):
            attributes = dir(HID.CODE)
            if(value in attributes):
                HID.press(bytes([0, 0, getattr(HID.CODE, value), *[0] * 5]))

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        for line in file:
            parse_line(line.strip())