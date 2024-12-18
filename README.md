# virtex
<img src ='https://github.com/user-attachments/assets/8c0a127d-172a-4b69-ba02-36b4c11f8f58' style='height:200px'/>
<img src ='https://github.com/user-attachments/assets/e4667d71-ee57-4f77-94bc-dcc0983403da' style='height:200px'/>


The VIRTEX Bridge device is a multifunction USB device that runs on the Raspberry Pi Zero 2 to provide the following capabilities:
- Enable Wi-Fi access as either a Host or Access Point
- Emulate peripheral USB devices like keyboards, mice, network adapters
- Invoke virtual hardware functions remotely with REST API and command line functions.
- Provide a developer-friendly hosting platform for side-loading useful sotware.

## Hardware Setup
Complete hardware setup is covered in the [Hardware Setup Guide](docs/HardwareSetup.md).

## Software Setup
```bash
git clone git@github.com:armunro/virtex.git
cd virtex/install
./install.sh
```

## Command Line Usage
```bash
# Run a VTXT step file 
vtx run --file ~/sample.vtxt.yaml

# Send text using an interactive terminal
vtx console

# Link references to bitwarden items and send them
vtx bw -l "my bitwarden item to search for"
vtx bw 
```

## REST API Usage
```bash
# STEP 1: Create localhost:5000->5000 SSH tunnel
# Ensure virtex-serve is running
systemctl status virtex-serve

# Type a multi-line document
POST http://localhost:5000/hid/kb/string
...body...

# Type a simple string
GET http://localhost:5000/hid/kb/string?text=Hello World!

# Run a vtxt file
GET http://localhost:5000/hid/kb/vtext?file=ytest.vtext

# Run send a bitwarden secret
GET http://localhost:5000/hid/kb/bw?ref=aspx.bwref.yaml&template={username}%09{password}%0A

# Send a file in the `virtex-data/files`
GET http://localhost:5000/hid/kb/bw?file=test2.txt
```