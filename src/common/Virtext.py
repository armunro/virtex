import yaml
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../" ))
import Keys
from alive_progress import alive_it

def yaml_to_compact_format(input_yaml: str) -> str:
    """Convert detailed YAML to compact format."""
    data = yaml.safe_load(input_yaml)
    compact_steps = []
    for step in data.get("steps", []):
        command = step.pop("command", None)
        if command:
            if step:  
                compact_steps.append({command: step})
            else: 
                compact_steps.append({command: None})
    return yaml.dump({"steps": compact_steps}, default_flow_style=False, sort_keys=False)

def yaml_to_detailed_format(compact_yaml: str) -> str:
    """Convert compact YAML back to detailed format."""
    data = yaml.safe_load(compact_yaml)
    detailed_steps = []
    for step in data.get("steps", []):
        for command, args in step.items():
            if args is None:  
                detailed_steps.append({"command": command})
            elif isinstance(args, dict):
                detailed_steps.append({"command": command, **args})
            elif isinstance(args, str): 
                detailed_steps.append({"command": command, "text": args})
            elif isinstance(args, int):
                detailed_steps.append({"command": command, "text": args})
    return yaml.dump({"steps": detailed_steps}, default_flow_style=False, sort_keys=False)


def exec_virtext_step(step):
    print(step)
    command = step["command"].lower()
    if (command == "print"):
        Keys.type_string(step["text"])
    elif (command == "launch"):
        Keys.launch_app(step["text"])
    elif (command == "sleep"):
        time.sleep(float(step["text"]))
    else:
        print("Unknown command "+ command)

           
def execute_step_file(scriptPath):
    with open(scriptPath, 'r') as file:
        file_contents = file.read()
        detailedYaml = yaml_to_detailed_format(file_contents)
        data = yaml.safe_load(detailedYaml)
        for step in data["steps"]:  
            exec_virtext_step(step)
        