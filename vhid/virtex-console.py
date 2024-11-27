#!/usr/bin/python3
import sys
from HID import CODE
import HID

def main():
    print("Enter your input (press Ctrl+D to exit):")
    try:
        while True:
            user_input = input()
            HID.type_string(user_input)
            print(f"SENT: {user_input}")
    except EOFError:
        print("\nExiting...")

if __name__ == "__main__":
    main()