dietpi-software install 9     # node
dietpi-software install 17    # git
dietpi-software install 130   # python

pip install pyyaml
pip install pick
pip install colorama
pip install tqdm
pip install python-dotenv
pip install flask

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

cp ./virtex.service /etc/systemd/system
cp ./virtex-start-usb /usr/bin

chmod +x /etc/systemd/system/virtex.service
chmod +x /usr/bin/virtex-start-usb