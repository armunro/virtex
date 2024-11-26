import os
import json
import subprocess

from dotenv import load_dotenv

def unlock_bitwarden():
    my_env = os.environ.copy()
    
    load_dotenv()
    if 'BW_SESSION' in os.environ:
            my_env["BW_SESSION"] = os.environ["BW_SESSION"]
    else:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        sessionId = subprocess.run(["/usr/local/bin/bw", "unlock", "--passwordfile=" + script_dir + "/master.bwpass.txt", "--raw"], capture_output=True, text=True).stdout
        my_env["BW_SESSION"] = sessionId
        with open(".env", 'w') as file:
            file.write("BW_SESSION=" + sessionId)
    return my_env

def get_item(id, env):
    result = subprocess.run(["/usr/local/bin/bw", "get", "item", id], capture_output=True, text=True, env=env)
    item = json.loads(result.stdout)
    return item


def create_ref(id, template="{username}\t{password}\n"):
    return {'id': id, 'template': template}

def calc_ref_path():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(script_dir,"refs")
    return path
