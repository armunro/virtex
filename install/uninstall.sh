#!/bin/bash

dietpi-software uninstall 9 # node.js
dietpi-software uninstall 17 # git
dietpi-software uninstall 130 # python3
npm uninstall -g @bitwarden/cli

#echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
#echo "dwc2" | sudo tee -a /etc/modules
#echo "libcomposite" | sudo tee -a /etc/modules

rm /usr/bin/virtex-start-usb

systemctl stop virtex
rm /etc/systemd/system/virtex.service
systemctl daemon-reload