#!/usr/bin/python3
    
import os
import subprocess
import shutil

python_packages = ["pyyaml", "pick", "colorama", "tqdm", "python-dotenv", "flask"]
node_packages = ["@bitwarden/cli"]
dietpi_packages = [9, 17, 130] # node, git, python
script_dir = os.path.dirname(os.path.abspath(__file__))
usb_start_script = os.path.join(script_dir, "part/vpm/virtex-start-usb")
service_file = os.path.join(script_dir, "part/service/virtex.service")

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error executing: {command}")
        exit(result.returncode)

def enable_usb_hid():
    with open("/boot/config.txt", "a") as f:
        f.write("dtoverlay=dwc2\n")

    with open("/etc/modules", "a") as f:
        f.write("dwc2\n")
        f.write("libcomposite\n")


def ensure_node_package_installed(package_name):
    try:
        result = subprocess.run(
            ["npm", "list", "-g", package_name, "--depth=0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if package_name in result.stdout:
            print(f"'{package_name}' is already installed.")
            return True
        
        print(f"Installing '{package_name}'...")
        install_result = subprocess.run(
            ["npm", "install", "-g", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if install_result.returncode == 0:
            print(f"'{package_name}' was successfully installed.")
            return True
        else:
            print(f"Failed to install '{package_name}'. Error: {install_result.stderr}")
            return False
    except FileNotFoundError:
        print("npm is not installed or not available in the PATH.")
        return False

for package in python_packages:
    run_command(f"pip install {package}")
    
for package in node_packages:
    ensure_node_package_installed(package)
    
for package in dietpi_packages:
    run_command(f"dietpi-software install {package}")

enable_usb_hid()  

if os.path.exists(usb_start_script):
    shutil.copy(usb_start_script, "/usr/bin")
    run_command("chmod +x /usr/bin/virtex-start-usb")
else:
    print(f"File not found: {usb_start_script}")
    exit(1)

if os.path.exists(service_file):
    shutil.copy(service_file, "/etc/systemd/system")
    run_command("systemctl daemon-reload")
    run_command("systemctl enable virtex")
else:
    print(f"File not found: {service_file}")
    exit(1)
