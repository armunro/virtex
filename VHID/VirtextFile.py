import Keys
from alive_progress import alive_it

def send_file(path):
    num_lines = Keys.line_count(path)
    # open file to read content
    with open(path, encoding='utf-8') as inp_file:
        for line in alive_it(inp_file, num_lines):  
            Keys.type_string(line)