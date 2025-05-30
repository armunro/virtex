#!/usr/bin/bash

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
    echo "alias vtx='python3 /root/virtex/src/cli/vtx.py'" | sudo tee -a /root/.bashrc > /dev/null
fi