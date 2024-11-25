#!/bin/bash

dietpi-software install 9 # node.js
dietpi-software install 17 # git
dietpi-software install 130 # python3
npm install -g @bitwarden/cli
apt install jq

echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules

cp ./virtex-start-usb /usr/bin
chmod +x /usr/bin/virtex-start-usb

cp ./virtex.service /etc/systemd/system
systemctl daemon-reload
systemctl enable virtex