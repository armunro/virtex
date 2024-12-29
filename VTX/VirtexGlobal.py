import os

def get_virtex_data_file(directory, extension):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(script_dir, "..","..", "virtex-data", directory)
    if not extension.startswith('.'):
        extension = f'.{extension}'    
    files = [file for file in os.listdir(path) if file.endswith(extension)]
    return files

def get_virtex_data_file_contents(directory, name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(script_dir, "..", "..","virtex-data", directory, name)
    with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()