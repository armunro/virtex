## Requirements 
This is an unattended install. You will require a computer write the initial image to the MicroSD card and subsequently manage and access it. This computer requires:
- MicroSD Card Reader
- Balena Etcher or Rufus
- XZip
- SSH or PuTTY (PuttyGen or ssh-keygen is required)

## Installation Steps

###  Flash SD Card
Dietpi documentation recommends using either Balena Etcher or Rufus but both tools write the Dietpi image to the MicroSD card.
- Download DietPi for Raspberry Pi 3/4/5 + Zero 2.
- Download Balena Etcher.
- Extract the DietPi .xz  archive.
- Use Etcher to write the *.iso file that was extracted.

### Generate SSH Key
Generate a public/private SSH key pair or use an existing public key.

### Configure Installation
Insert the SD card into a card reader and open in explorer. The following files are used to configure the install, and overall system settings.

#### dietpi.txt
This file configures the main dietpi install settings. [More details and configuration option here.](https://dietpi.com/docs/usage/#network-configuration)
```
AUTO_SETUP_KEYBOARD_LAYOUT=en
AUTO_SETUP_TIMEZONE=America/Regina
AUTO_SETUP_NET_WIFI_ENABLED=1 
AUTO_SETUP_NET_WIFI_COUNTRY_CODE=CA
AUTO_SETUP_NET_HOSTNAME=VIRTEX-R1-B
AUTO_SETUP_HEADLESS=1 
AUTO_SETUP_SSH_PUBKEY=ssh... # Put an SSH allowed public key here 
AUTO_SETUP_AUTOMATED=1 
AUTO_SETUP_GLOBAL_PASSWORD=flyingkomodo
SURVEY_OPT_IN=0    
```
#### dietpi-wifi.txt
The file is self explanitory but it contains an array structure of wireless networks, the names (SSIDs) and passwords (WPA-PSK). It is important to have one known network configured before first boot. Wifi networks can be added later using the `dietpi-wifidb` command.
### Finalize

- Safely eject the MicroSD card and insert it into the Pi Zero.
  

### First-boot Install
Once the PI is started, the txt config files are never read again. Subsequent changes must be done in the shell on the device.

NOTE: In the standard FLIRC grey/black case provided, The status LED can be difficult to see. It can be seen somewhat when looking into the device through the top power usb port.
The process of the install and startup can be monitored by watching the status LED. Faster binking implies the startup scripts are still running.

- Insert the MicroSD and connect a USB cable to the USB port labeled "USB" (The middle port)
The automated install will take ~5m. Keep the device on as long as the LED is blinking or changing blink patterns consistently.
- Locate the device's IP address by one of the following
Check your router's DHCP leases or ARP tables for `VIRTEX-R1-A|B|C|...` 
- If you know the devices MAC address, commands like `arp -a` can be helpful for matching the hardware address to the IP.
- Use a tool like Nmap to scan the network for port 22:ssh 
SSH into the device using the IP address. Use the generated private key (optional) or use standard default credentials:
  - Username: `root` 
  - Password: `flyingkomodo`