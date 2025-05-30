import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../" ))

import Keys
from alive_progress import alive_it

def send_file(path):
    line_count = Keys.line_count(path)
    with open(path, encoding='utf-8') as file:
        for line in alive_it(file, line_count):  
            Keys.type_string(line)