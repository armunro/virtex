import Keys
import Virtext

def show_console():
    print("Enter your input (press Ctrl+D to exit):")
    try:
        while True:
            user_input = input()
            print(f"SENT: {user_input}")
    except EOFError:
        print("\nExiting...")