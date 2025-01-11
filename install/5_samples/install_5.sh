#!/usr/bin/bash

SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cp -f $SCRIPT_ROOT/sample-vtext/* /root/virtex-data/vtext
cp -f $SCRIPT_ROOT/sample-files/* /root/virtex-data/files