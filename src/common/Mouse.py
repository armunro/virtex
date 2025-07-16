# mouse_hid.py
import time
import os
from dataclasses import dataclass

# Path to the HID gadget for the mouse
HID_MOUSE = '/dev/hidg1'

# Button masks
BUTTON_LEFT = 0x01
BUTTON_RIGHT = 0x02
BUTTON_MIDDLE = 0x04

@dataclass
class Mouse:
    """High level mouse helper for HID gadget."""

    device: str = HID_MOUSE

    def _write(self, buttons: int = 0, x: int = 0, y: int = 0, wheel: int = 0) -> None:
        report = bytes([
            buttons & 0x07,
            x & 0xFF,
            y & 0xFF,
            wheel & 0xFF,
        ])
        with open(self.device, "wb+") as f:
            f.write(report)

    def move(self, x: int, y: int, delay: float = 0.01) -> None:
        self._write(x=x, y=y)
        time.sleep(delay)
        self._write()

    def click(self, button: int = BUTTON_LEFT, delay: float = 0.05) -> None:
        self._write(buttons=button)
        time.sleep(delay)
        self._write()

    def scroll(self, wheel: int, delay: float = 0.01) -> None:
        self._write(wheel=wheel)
        time.sleep(delay)
        self._write()

    def drag(self, x: int, y: int, button: int = BUTTON_LEFT, delay: float = 0.01) -> None:
        self._write(buttons=button)
        time.sleep(0.01)
        self.move(x, y, delay=delay)
        self._write()


# backward compatible helper instance
mouse = Mouse()

def send_mouse_report(buttons=0, x=0, y=0, wheel=0):
    mouse._write(buttons, x, y, wheel)

def move(x, y, delay=0.01):
    mouse.move(x, y, delay)

def click(button=BUTTON_LEFT, delay=0.05):
    mouse.click(button, delay)

def scroll(amount, delay=0.01):
    mouse.scroll(amount, delay)

def drag(x, y, button=BUTTON_LEFT, delay=0.01):
    mouse.drag(x, y, button, delay)

def example_usage():
    time.sleep(2.0)
    move(20, 20)
    time.sleep(0.2)
    click(BUTTON_RIGHT)

if __name__ == '__main__':
    if not os.path.exists(HID_MOUSE):
        raise FileNotFoundError(f"{HID_MOUSE} not found. Is the HID gadget configured?")
    example_usage()
