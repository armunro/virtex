#!/usr/bin/env python3

import os
import sys
import time
from pathlib import Path

BASE_DIR = Path("/sys/kernel/config/usb_gadget")
GADGET_NAME = "virtex"
GADGET_DIR = BASE_DIR / GADGET_NAME
UDC_PATH = Path("/sys/class/udc")

KEYBOARD_REPORT_DESC = (
    b'\x05\x01\x09\x06\xa1\x01\x05\x07\x19\xe0\x29\xe7\x15\x00\x25\x01\x75\x01\x95\x08\x81\x02'
    b'\x95\x01\x75\x08\x81\x03\x95\x05\x75\x01\x05\x08\x19\x01\x29\x05\x91\x02\x95\x01\x75\x03'
    b'\x91\x03\x95\x06\x75\x08\x15\x00\x25\x65\x05\x07\x19\x00\x29\x65\x81\x00\xc0'
)

MOUSE_REPORT_DESC = (
    b'\x05\x01\x09\x02\xa1\x01\x09\x01\xa1\x00\x05\x09\x19\x01\x29\x03\x15\x00\x25\x01\x95\x03'
    b'\x75\x01\x81\x02\x95\x01\x75\x05\x81\x03\x05\x01\x09\x30\x09\x31\x15\x81\x25\x7f\x75\x08'
    b'\x95\x02\x81\x06\xc0\xc0'
)

def write(path, content):
    with open(path, 'wb' if isinstance(content, bytes) else 'w') as f:
        f.write(content)

def get_udc():
    return next(UDC_PATH.iterdir()).name

def create_base():
    if not GADGET_DIR.exists():
        print("Creating base gadget...")
        GADGET_DIR.mkdir(parents=True)
        write(GADGET_DIR / "idVendor", "0x1d6b")
        write(GADGET_DIR / "idProduct", "0x0104")
        write(GADGET_DIR / "bcdDevice", "0x0100")
        write(GADGET_DIR / "bcdUSB", "0x0200")

        strings = GADGET_DIR / "strings/0x409"
        strings.mkdir(parents=True)
        write(strings / "serialnumber", "fedcba9876543210")
        write(strings / "manufacturer", "Andrew Munro")
        write(strings / "product", "Virtex USB HID Bridge")

        config = GADGET_DIR / "configs/c.1/strings/0x409"
        config.mkdir(parents=True)
        write(config / "configuration", "Config 1: HID composite")
        write(GADGET_DIR / "configs/c.1/MaxPower", "250")

def link_function(name):
    config_path = GADGET_DIR / "configs/c.1"
    func_path = GADGET_DIR / f"functions/{name}"
    if not (config_path / name).exists():
        os.symlink(func_path, config_path / name)

def unlink_function(name):
    config_link = GADGET_DIR / "configs/c.1" / name
    if config_link.exists():
        config_link.unlink()

def remove_function(name):
    unlink_function(name)
    func_path = GADGET_DIR / f"functions/{name}"
    if func_path.exists():
        for file in func_path.iterdir():
            file.unlink()
        func_path.rmdir()

def bind():
    write(GADGET_DIR / "UDC", get_udc())

def unbind():
    write(GADGET_DIR / "UDC", "")

def start_function(fn):
    create_base()

    if fn == "keyboard":
        path = GADGET_DIR / "functions/hid.usb0"
        if not path.exists():
            path.mkdir()
            write(path / "protocol", "1")
            write(path / "subclass", "1")
            write(path / "report_length", "8")
            write(path / "report_desc", KEYBOARD_REPORT_DESC)
            link_function("hid.usb0")
            print("Keyboard started.")
    elif fn == "mouse":
        path = GADGET_DIR / "functions/hid.usb1"
        if not path.exists():
            path.mkdir()
            write(path / "protocol", "2")
            write(path / "subclass", "1")
            write(path / "report_length", "3")
            write(path / "report_desc", MOUSE_REPORT_DESC)
            link_function("hid.usb1")
            print("Mouse started.")
    bind()

def stop_function(fn):
    if not GADGET_DIR.exists():
        print("No gadget to stop.")
        return
    unbind()
    if fn == "keyboard":
        remove_function("hid.usb0")
        print("Keyboard stopped.")
    elif fn == "mouse":
        remove_function("hid.usb1")
        print("Mouse stopped.")
    bind()  # Rebind with remaining functions

def cleanup_all():
    if not GADGET_DIR.exists():
        return
    print("Cleaning up all gadgets...")
    unbind()
    stop_function("keyboard")
    stop_function("mouse")
    for p in ["configs/c.1/strings/0x409", "configs/c.1", "strings/0x409"]:
        try:
            (GADGET_DIR / p).rmdir()
        except:
            pass
    GADGET_DIR.rmdir()
    print("Cleaned up.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: virtex_usb.py [start|stop|cleanup] [keyboard|mouse|all]")
        sys.exit(1)

    action = sys.argv[1].lower()
    target = sys.argv[2].lower()

    if action == "start":
        if target in ["keyboard", "mouse"]:
            start_function(target)
    elif action == "stop":
        if target in ["keyboard", "mouse"]:
            stop_function(target)
    elif action == "cleanup" and target == "all":
        cleanup_all()
    else:
        print("Invalid arguments.")
