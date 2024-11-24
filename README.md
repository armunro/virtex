# virtex
Companion hardware for busy people.

## Introduction
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
./installVirtex.sh
```