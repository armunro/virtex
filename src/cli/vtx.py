
#!/usr/bin/python3
import argparse
import VirtexConsole
import src.common.Virtext
import src.common.Keys
import src.common.Mouse

### CLI Parser
parser = argparse.ArgumentParser(description="Virtex")
subparsers = parser.add_subparsers(dest='command', help='Subcommands')

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
    src.common.Virtext.execute_step_file(args.file)
elif args.command == 'cat':
    src.common.Virtext.send_file(args.file)
else:
    parser.print_help()
