#!/usr/bin/python3
from flask import Flask, request, Response, send_from_directory, render_template, stream_with_context
import sys
import subprocess
import os
import time
from urllib.parse import quote

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../common" ))


import VirtexGlobal
import Keys
import Virtext




app = Flask(__name__, static_folder='static', static_url_path='/assets', template_folder='templates')

@app.route('/')
def home():
    return send_from_directory('static', "dashboard.html")

@app.route('/hid/kb/string', methods=['POST'])
def receive_string_post():
    data = request.data.decode('utf-8')  
    Keys.type_string(data)
    
@app.route('/hid/kb/string', methods=['GET'])
def receive_string_get():
    text = request.args.get('text')
    Keys.type_string(text)
    return f"SENT: {text}"


@app.route('/hid/kb/vtext', methods=['GET'])
def run_vtext_get():
    text = request.args.get('file')
    script_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(script_dir, "..", "..", ".." ,"virtex-data", "vtext", text)
    Virtext.execute_step_file(path)
    return f"RAN: {path}"

@app.route('/hid/kb/templates', methods=['GET'])
def get_templates():
    return [
        {"text": "Username", "value": "{username}"},
        {"text": "Password", "value": "{password}"},
        {"text": "Password[E]", "value": "{password}" + quote("\n")},
        {"text": "User[T]Pass[E]", "value": "{username}" + quote("\t") + "{password}" + quote("\n")}
    ]

@app.route('/hid/kb/methods', methods=['GET'])
def get_methods():
    return {
        "vtext": {
            "display": "VTEXT",
            "icon": "fas fa-code",
            "endpoint": "/hid/kb/vtext",
            "items": Virtext.get_virtex_data_file("vtext", "vtext")
        },
        "files": {
            "display": "Files",
            "icon": "fas fa-file",
            "endpoint": "/hid/kb/bw",
            "items": Virtext.get_virtex_data_file("files", "txt")
        }
    }
    
@app.route("/whatever", methods=["GET","POST"])
def whatever():
    def generate_output():
        with subprocess.Popen(
                "ping -c 5 8.8.8.8",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True) as proc:
            for line in proc.stdout:
                yield line

    return Response(generate_output(), mimetype='text/plain')