# virtex
![device](https://github.com/user-attachments/assets/8c0a127d-172a-4b69-ba02-36b4c11f8f58)![virtex-overview](https://github.com/user-attachments/assets/e4667d71-ee57-4f77-94bc-dcc0983403da)

The VIRTEX Bridge device is a multifunction peripheral that runs on the Raspberry Pi Zero 2 to provide the following capabilities:
- Enable Wi-Fi access as either a Host or Access Point
- Emulate peripheral USB devices like keyboards, mice, network adapters
- Invoke virtual hardware functions remotely with REST API and command line functions.
- Provide a developer-friendly hosting platform for side-loading useful sotware.

## Hardware Setup
Complete hardware setup is covered in the [Hardware Setup Guide](docs/HardwareSetup.md).

## Software Setup
```bash
git clone git@github.com:armunro/virtex.git
cd virtex/install
./install.sh
```
## Functions

### Keyboard 
- [Bitwarden](docs/Bitwarden.md) - Automated credential entry.
- Console - `vtx-console` for direct text entry.
- VirText - Keyboard automation scripting with `vtx-vtxt`
