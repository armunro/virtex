#!/usr/bin/python3
from flask import Flask, request, send_from_directory, render_template
import sys
import VirtexGlobal
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"VHID" ))
import Keys
import Virtext
import time


app = Flask(__name__, static_folder='HTTP/static', static_url_path='/assets', template_folder='HTTP/templates')

@app.route('/')
def home():
    data = {
        "title": "Virtex Dashboard",
        "heading": "Virtex Dashboard",
        "bitwardenItems": VirtexGlobal.get_virtex_data_file("bitwarden", "bwref.yaml"),
        "vtextItems": VirtexGlobal.get_virtex_data_file("vtext", "vtext")
    }
    return render_template('dash.html', **data)


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
    return f"RAN: {path}"

@app.route('/static-html')
def serve_static_html():
    return send_from_directory('static', 'example.html')