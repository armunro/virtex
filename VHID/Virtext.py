#!/usr/bin/python3
import yaml
import time
import Keys
import VirtexBitwarden
from alive_progress import alive_it

def yaml_to_compact_format(input_yaml: str) -> str:
    """Convert detailed YAML to compact format."""
    data = yaml.safe_load(input_yaml)
    compact_steps = []
    for step in data.get("steps", []):
        command = step.pop("command", None)
        if command:
            if step:  # If there are additional key-value pairs
                compact_steps.append({command: step})
            else:  # If there's only the command
                compact_steps.append({command: None})
    return yaml.dump({"steps": compact_steps}, default_flow_style=False, sort_keys=False)

def yaml_to_detailed_format(compact_yaml: str) -> str:
    """Convert compact YAML back to detailed format."""
    data = yaml.safe_load(compact_yaml)
    detailed_steps = []
    for step in data.get("steps", []):
        for command, args in step.items():
            print(command)
            print(args)
            if args is None:  # Command with no arguments
                detailed_steps.append({"command": command})
            elif isinstance(args, dict):  # Command with arguments
                detailed_steps.append({"command": command, **args})
            elif isinstance(args, str):  # Command with a single string argument
                detailed_steps.append({"command": command, "text": args})
            elif isinstance(args, int):  # Command with a single string argument
                detailed_steps.append({"command": command, "text": args})
    return yaml.dump({"steps": detailed_steps}, default_flow_style=False, sort_keys=False)


def exec_virtext_step(step):
    command = step["command"].lower()
    if (command == "print"):
        Keys.type_string(step["text"])
    elif (command == "launch"):
        Keys.launch_app(step["text"])
    elif (command == "sleep"):
        time.sleep(float(step["text"]))
    elif (command == "bitwarden"):
        VirtexBitwarden.send_bitwarden_item2(step["ref"], step["template"])
    else:
        print("Unknown command "+ command)

           
def execute_step_file(scriptPath):
    with open(scriptPath, 'r') as file:
        file_contents = file.read()
        detailedYaml = yaml_to_detailed_format(file_contents)
        data = yaml.safe_load(detailedYaml)
        for step in alive_it(data["steps"]):  
            exec_virtext_step(step)
        