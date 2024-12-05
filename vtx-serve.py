#!/usr/bin/python3
from flask import Flask
from flask import request
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"VHID" ))
import Keys
import Virtext

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World2!</p>"

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
    path = os.path.join(script_dir, "..","virtex-data", "vtext", text)
    Virtext.execute_step_file(path)
    return f"SENT: {path}"