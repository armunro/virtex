#!/usr/bin/python3
import argparse
import subprocess
import os
import sys


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"VHID" ))
import Keys
import VirtexBitwarden
import VirtexConsole
import Virtext
import VirtextFile


### CLI Parser
parser = argparse.ArgumentParser(description="Virtex")
subparsers = parser.add_subparsers(dest='command', help='Subcommands')

# Cat
parse_vtxt2 = subparsers.add_parser('cat', help='Echo a text file to the VHID.')
parse_vtxt2.add_argument('file')
# Vtxt
parse_vtxt = subparsers.add_parser('run', help='Replay HID automation files remotely.')
parse_vtxt.add_argument('file')
# Console
parse_console = subparsers.add_parser('console', help='Interactive terminal with remote text entry.')
# Bitwarden
parse_bw = subparsers.add_parser('bitwarden', help='Automated BW item entry', aliases=['bw'] )
parse_bw.add_argument("-r", "--ref", help='The bitwarden reference to type.' )




args = parser.parse_args()

if args.command in ["bw", "bitwarden"]:
    if(args.ref):
        VirtexBitwarden.create_bwref(args.ref)
    else:
        VirtexBitwarden.send_bitwarden_item()
elif args.command == 'console':
    VirtexConsole.show_console()
elif args.command == 'run':
    Virtext.execute_step_file(args.file)
elif args.command == 'cat':
    VirtextFile.send_file(args.file)
else:
    parser.print_help()