# virtex

The VIRTEX Bridge device is a multifunction USB device that runs on the Raspberry Pi Zero 2 to provide the following capabilities:
- Enable Wi-Fi access as either a Host or Access Point
- Emulate peripheral USB devices like keyboards, mice, network adapters
- Invoke virtual hardware functions remotely with REST API and command line functions.
- Provide a developer-friendly hosting platform for side-loading useful sotware.



## Hardware Setup
Complete hardware setup is covered in the [Hardware Setup Guide](docs/HardwareSetup.md).

## Software Setup
```bash
# Add your SSH key
eval `ssh-agent`
ssh-add ~/.ssh/GITHUB_KEY_FILE
git clone git@github.com:armunro/virtex.git
cd virtex/install
./install.sh
```
## Main Service control
```bash
# Enable and start the WebUI (Not needed after install)
systemctl enable virtex-web
systemctl start virtex-web

# Enable and start the HID service (Keyboard+Mouse) (Not needed after install)
systemctl enable virtex-hid
systemctl start virtex-hid
```
## How Does it Work?
`libcomposite` is a Linux kernel module that can emulate USB devices. These virtual usb devices are sometimes referred to as 'gadgets'. When supported by the Raspberry Pi Zero 2 and other Single Board Computers (SBCs), we have a robust and _relatively_ simple platform for tooling. Virtex adds simple python APIs, functions and interfaces.
## Directory Structures
```bash
/root
  /virtex
    /src         # All of the code
      /api         # HTTP Api for invoking functions
      /cli         # Command line tools for automation
      /common      # Shared code
      /ui          # Precompiled web frontend
```

## Command Line Usage
See [VTEXT2 specification](docs/VTEXT2.md) for the advanced automation syntax.
```bash
# Run a VTXT step file 
vtx run /root/virtex-data/websearch_sample.vtext

# Send text using an interactive terminal
vtx console

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

# Send a file in the `virtex-data/files`
GET http://localhost:5000/hid/kb/bw?file=test2.txt
```
