/boot/dietpi/dietpi-software install 9     # node
/boot/dietpi/dietpi-software install 17    # git
/boot/dietpi/dietpi-software install 130   # python

pip install pyyaml
pip install pick
pip install colorama
pip install tqdm
pip install python-dotenv
pip install flask
pip install alive_progress
npm install -g @bitwarden/cli


# Add dtoverlay=dwc2 to /boot/config.txt if not already present
if ! grep -Fxq "dtoverlay=dwc2" /boot/config.txt; then
    echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt > /dev/null
fi

# Add dwc2 to /etc/modules if not already present
if ! grep -Fxq "dwc2" /etc/modules; then
    echo "dwc2" | sudo tee -a /etc/modules > /dev/null
fi

# Add libcomposite to /etc/modules if not already present
if ! grep -Fxq "libcomposite" /etc/modules; then
    echo "libcomposite" | sudo tee -a /etc/modules > /dev/null
fi
# Add aliases to .bashrc
if ! grep -Fxq "vtx.py" /root/.bashrc; then
    echo "alias vtx='python3 /root/virtex/vtx.py'" | sudo tee -a /root/.bashrc > /dev/null
fi

mkdir /root/virtex-data
mkdir /root/virtex-data/bitwarden
mkdir /root/virtex-data/vtext
mkdir /root/virtex-data/files

cp -f ./virtex.service /etc/systemd/system
cp -f ./virtex-serve.service /etc/systemd/system
cp -f ./virtex-start-usb /usr/bin

chmod +x /etc/systemd/system/virtex.service
chmod +x /etc/systemd/system/virtex.service
chmod +x /usr/bin/virtex-start-usb

systemctl daemon-reload
systemctl enable virtex
systemctl enable virtex-serve
