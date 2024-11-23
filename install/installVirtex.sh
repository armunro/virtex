#!/bin/bash

cp ./virtex-start-usb /usr/bin
chmod +x /usr/bin/virtex-start-usb

cp ./virtex.service /etc/systemd/system
systemctl daemon-reload
systemctl enable virtex
