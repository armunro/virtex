#!/usr/bin/bash

SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Virtex USB 
cp -f $SCRIPT_ROOT/virtex-usb.service /etc/systemd/system
chmod +x /etc/systemd/system/virtex-usb.service

# Virtex Start USB
cp -f $SCRIPT_ROOT/virtex-start-usb /usr/bin
chmod +x /usr/bin/virtex-start-usb

# Virtex Web
cp -f $SCRIPT_ROOT/virtex-web.service /etc/systemd/system
chmod +x /etc/systemd/system/virtex-web.service

systemctl daemon-reload
systemctl enable virtex-usb
systemctl enable virtex-web