import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../" ))
from VTXHid import Keys
from VTXHid import Virtext

def show_console():
    print("Enter your input (press Ctrl+D to exit):")
    try:
        while True:
            user_input = input()
            print(f"SENT: {user_input}")
    except EOFError:
        print("\nExiting...")