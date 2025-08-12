#!/usr/bin/bash

SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Virtex USB 
cp -f $SCRIPT_ROOT/virtex-hid.service /etc/systemd/system
chmod +x /etc/systemd/system/virtex-hid.service

# Virtex Start USB
cp -f $SCRIPT_ROOT/virtex-hid-start /usr/bin
chmod +x /usr/bin/virtex-hid-start

# Virtex Web
cp -f $SCRIPT_ROOT/virtex-web.service /etc/systemd/system
chmod +x /etc/systemd/system/virtex-web.service

# Virtex Ghost Script
cp -f $SCRIPT_ROOT/virtex-ghost.service /etc/systemd/system
chmod +x /etc/systemd/system/virtex-ghost.service

systemctl daemon-reload
systemctl enable virtex-hid
systemctl enable virtex-web
systemctl enable virtex-ghost