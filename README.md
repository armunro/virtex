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


## Command Line Usage
See [VTEXT2 specification](docs/VTEXT2.md) for the advanced automation syntax.
```bash
usage: vtx.py [-h] {echo,cat,console,launch,run,update} ...

Virtex

positional arguments:
  {echo,cat,console,launch,run,update}
                        Subcommands
    echo                Send a string to the target
    cat                 Send a text file to the target.
    console             Interactive terminal with remote text entry.
    launch              Open an application or file using the run dialog.
    run                 Replay HID automation files remotely.
    update              Get the latest copy of Virtex

options:
  -h, --help            show this help message and exit
```
