# mouse_hid.py
import time
import os

# Path to the HID gadget for the mouse
HID_MOUSE = '/dev/hidg1'

# Button masks
BUTTON_LEFT = 0x01
BUTTON_RIGHT = 0x02
BUTTON_MIDDLE = 0x04

def send_mouse_report(buttons=0, x=0, y=0, wheel=0):
    """
    Send a mouse HID report.
    buttons: bitmask (LEFT=1, RIGHT=2, MIDDLE=4)
    x, y: signed char deltas (-127 to 127)
    wheel: signed char for scroll (e.g., 1 = scroll up, -1 = scroll down)
    """
    report = bytes([
        buttons & 0x07,  # Buttons (1 byte)
        x & 0xFF,        # X movement (1 byte)
        y & 0xFF,        # Y movement (1 byte)
        wheel & 0xFF     # Wheel movement (1 byte)
    ])
    with open(HID_MOUSE, 'wb+') as f:
        f.write(report)

def move(x, y, delay=0.01):
    send_mouse_report(x=x, y=y)
    time.sleep(delay)
    send_mouse_report()  # release

def click(button=BUTTON_LEFT, delay=0.05):
    send_mouse_report(buttons=button)
    time.sleep(delay)
    send_mouse_report()

def example_usage():
    time.sleep(2.0)
    move(20, 20)
    time.sleep(0.2)
    click(BUTTON_RIGHT)

if __name__ == '__main__':
    if not os.path.exists(HID_MOUSE):
        raise FileNotFoundError(f"{HID_MOUSE} not found. Is the HID gadget configured?")
    example_usage()
