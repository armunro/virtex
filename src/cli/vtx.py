
#!/usr/bin/python3
import argparse
import VirtexConsole
import sys
import os


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../common" ))

import Virtext
import Keys
import Mouse

### CLI Parser
parser = argparse.ArgumentParser(description="Virtex")
subparsers = parser.add_subparsers(dest='command', help='Subcommands')

# Echo
parse_echo = subparsers.add_parser('echo', help='Type text to the target')
parse_echo.add_argument('text')

# Launch
parse_launch = subparsers.add_parser('launch', help='Open an application or file using the run dialog.')
parse_launch.add_argument('path')

# Update
parse_update = subparsers.add_parser('update', help='Retrieve the latest copy of Virtex')

# Cat
parse_vtxt = subparsers.add_parser('cat', help='Echo a text file to the VHID.')
parse_vtxt.add_argument('file')

# Vtxt
parse_vtxt = subparsers.add_parser('run', help='Replay HID automation files remotely.')
parse_vtxt.add_argument('file')

# Console
parse_console = subparsers.add_parser('console', help='Interactive terminal with remote text entry.')




args = parser.parse_args()

if args.command == 'console':
    VirtexConsole.show_console()
elif args.command == 'update':
    VirtexConsole.show_console() #todo
elif args.command == 'test':
    VirtexConsole.show_console() #todo
elif args.command == 'run':
    Virtext.execute_step_file(args.file)
elif args.command == 'cat':
    Virtext.send_file(args.file)
elif args.command == 'echo':
    Keys.type_string(args.text)
elif args.command == 'launch':
    Keys.launch_app(args.path)
else:
    parser.print_help()
