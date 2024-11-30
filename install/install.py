#!/usr/bin/python3
    
import os
import subprocess
import shutil

def run_command(command):
    """Run a shell command and exit on failure."""
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error executing: {command}")
        exit(result.returncode)
import subprocess

def ensure_node_package_installed(package_name):
    """
    Ensures a Node.js package is installed globally. Installs it if not found.
    
    Parameters:
        package_name (str): The name of the Node.js package to check and install.
    
    Returns:
        bool: True if the package is successfully installed, False otherwise.
    """
    try:
        # Check if the package is installed globally
        result = subprocess.run(
            ["npm", "list", "-g", package_name, "--depth=0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if package_name in result.stdout:
            print(f"'{package_name}' is already installed.")
            return True
        
        # If not installed, install the package globally
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

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Install DietPi software
#run_command("dietpi-software install 9")  # Node.js
#run_command("dietpi-software install 17")  # Git
#run_command("dietpi-software install 130")  # Python3

# Install npm and Python packages
run_command("npm install -g @bitwarden/cli")

python_packages = ["pyyaml", "pick", "colorama", "tqdm", "python-dotenv", "flask"]
for package in python_packages:
    run_command(f"pip install {package}")

# Install `jq` package
run_command("apt install -y jq")

# Update configuration files
with open("/boot/config.txt", "a") as f:
    f.write("dtoverlay=dwc2\n")

with open("/etc/modules", "a") as f:
    f.write("dwc2\n")
    f.write("libcomposite\n")

# Copy and set permissions for scripts and services
usb_start_script = os.path.join(script_dir, "part/vpm/virtex-start-usb")
if os.path.exists(usb_start_script):
    shutil.copy(usb_start_script, "/usr/bin")
    run_command("chmod +x /usr/bin/virtex-start-usb")
else:
    print(f"File not found: {usb_start_script}")
    exit(1)

service_file = os.path.join(script_dir, "part/service/virtex.service")
if os.path.exists(service_file):
    shutil.copy(service_file, "/etc/systemd/system")
    run_command("systemctl daemon-reload")
    run_command("systemctl enable virtex")
else:
    print(f"File not found: {service_file}")
    exit(1)
