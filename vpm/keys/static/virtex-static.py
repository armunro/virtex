#!/usr/bin/python3
import HID
import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        content = file.read()
        HID.type_string(content)