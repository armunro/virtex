import Keys

def show_console():
    print("Enter your input (press Ctrl+D to exit):")
    try:
        while True:
            user_input = input()
            Keys.type_string(user_input)
            print(f"SENT: {user_input}")
    except EOFError:
        print("\nExiting...")