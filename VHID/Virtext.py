#!/usr/bin/python3
import yaml
import time
import Keys
from alive_progress import alive_it


def exec_virtext_step(step):
    print(step)
    
    command = step["command"].lower()
    if (command == "print"):
        Keys.type_string(step["text"])
    elif (command == "launch"):
        Keys.launch_app(step["path"])
    elif (command == "sleep"):
        time.sleep(float(step["delay"]))
    elif (command == "search"):
        Keys.open_search(step["query"])
    else:
        print("Unknown command "+ command)

def execute_virtext_file(scriptPath):
    with open(scriptPath, "r") as file:
        data = yaml.safe_load(file)
        for step in alive_it(data["steps"]):  
            exec_virtext_step(step)