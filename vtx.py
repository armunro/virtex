#!/usr/bin/python3
import argparse
import subprocess
import os
import sys


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"VHID" ))
import Keys
import VirtexBitwarden
import VirtexLorem
import VirtexConsole
import Virtext

### CLI Parser
parser = argparse.ArgumentParser(description="Virtex")
subparsers = parser.add_subparsers(dest='command', help='Subcommands')

# Bitwarden
parse_bw = subparsers.add_parser('bitwarden', help='Automated BW item entry', aliases=['bw'] )
parse_bw.add_argument("-r", "--ref", help='The bitwarden reference to type.' )
# Console
parse_console = subparsers.add_parser('console', help='Interactive terminal with remote text entry.')
# Lorem
parse_lorem = subparsers.add_parser('lorem', help='Lorem Ipsum output.')
parse_lorem.add_argument('paragraphs', type=int)
# Vtxt
parse_lorem = subparsers.add_parser('vtxt', help='Replay HID automation files remotely.')
parse_lorem.add_argument('file')
args = parser.parse_args()

if args.command in ["bw", "bitwarden"]:
    if(args.ref):
        VirtexBitwarden.create_bwref(args.ref)
    else:
        VirtexBitwarden.send_bitwarden_item()
elif args.command == 'console':
    VirtexConsole.show_console()
elif args.command == 'lorem':
    VirtexLorem.generate_lorem(args.paragraphs)
elif args.command == 'vtxt':
    Virtext.execute_virtext_file(args.file)
else:
    parser.print_help()