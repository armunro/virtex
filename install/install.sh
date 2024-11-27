#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

dietpi-software install 9 # node.js
dietpi-software install 17 # git
dietpi-software install 130 # python3
npm install -g @bitwarden/cli
pip install pyyaml
pip install pick
pip install colorama
pip install tqdm
pip install python-dotenv


apt install jq

echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules

cp $SCRIPT_DIR/part/vpm/virtex-start-usb /usr/bin
chmod +x /usr/bin/virtex-start-usb

cp $SCRIPT_DIR/part/service/virtex.service /etc/systemd/system
systemctl daemon-reload
systemctl enable virtex