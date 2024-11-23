#!/usr/bin/python3
import sys
import os
import time
import HID
import json
import subprocess
from HID import CODE

if __name__ == "__main__":
    itemId = sys.argv[1]
    my_env = os.environ.copy()
    sessionId = subprocess.run(["/usr/local/bin/bw", "unlock", "--passwordfile=bw-password.txt", "--raw"], capture_output=True, text=True).stdout
    my_env["BW_SESSION"] = sessionId

    resultJson = subprocess.run(["/usr/local/bin/bw", "get", "item", itemId], capture_output=True, text=True, env=my_env).stdout
    secret = json.loads(resultJson)
    password = secret["login"]["password"]
    HID.type_string(password)
