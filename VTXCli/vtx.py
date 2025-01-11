<<<<<<< HEAD
#!/usr/bin/python3
import argparse
import subprocess
import os
import sys


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../" ))
from VTX import VirtexGlobal
from VTXHid import Keys
from VTXHid import Virtext
from VTXBitwarden import Bitwarden
from VTXCli import VirtexConsole
from VTXHid import Virtext
from VTXHid import VirtextFile


### CLI Parser
parser = argparse.ArgumentParser(description="Virtex")
subparsers = parser.add_subparsers(dest='command', help='Subcommands')

# Cat
parse_vtxt = subparsers.add_parser('cat', help='Echo a text file to the VHID.')
parse_vtxt.add_argument('file')
# Vtxt
parse_vtxt = subparsers.add_parser('run', help='Replay HID automation files remotely.')
parse_vtxt.add_argument('file')
# Console
parse_console = subparsers.add_parser('console', help='Interactive terminal with remote text entry.')
# Bitwarden
parse_bw = subparsers.add_parser('bitwarden', help='Automated Bitwarden Entry', aliases=['bw'] )
parse_bw.add_argument("-l", "--link", help='A search tearm to look for in Bitwarden' )




args = parser.parse_args()

if args.command in ["bw", "bitwarden"]:
    if(args.link):
        Bitwarden.create_bwref(args.link)
    else:
        Bitwarden.send_bitwarden_item()
elif args.command == 'console':
    VirtexConsole.show_console()
elif args.command == 'run':
    Virtext.execute_step_file(args.file)
elif args.command == 'cat':
    VirtextFile.send_file(args.file)
else:
    parser.print_help()
=======
#!/usr/bin/python3
import argparse
import subprocess
import os
import sys


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../" ))
from VTX import VirtexGlobal
from VTXHid import Keys
from VTXHid import Virtext
from VTXBitwarden import Bitwarden
from VTXCli import VirtexConsole
from VTXHid import Virtext
from VTXHid import VirtextFile


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
# Bitwarden
parse_bw = subparsers.add_parser('bitwarden', help='Automated Bitwarden Entry', aliases=['bw'] )
parse_bw.add_argument("-l", "--link", help='A search tearm to look for in Bitwarden' )




args = parser.parse_args()

if args.command in ["bw", "bitwarden"]:
    if(args.link):
        Bitwarden.create_bwref(args.link)
    else:
        Bitwarden.send_bitwarden_item()
elif args.command == 'console':
    VirtexConsole.show_console()
elif args.command == 'update':
    VirtexConsole.show_console() #todo
elif args.command == 'test':
    VirtexConsole.show_console() #todo
elif args.command == 'run':
    Virtext.execute_step_file(args.file)
elif args.command == 'cat':
    VirtextFile.send_file(args.file)
else:
    parser.print_help()
    
>>>>>>> 4d807a6 (Refactor)
