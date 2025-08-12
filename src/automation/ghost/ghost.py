#!/usr/bin/env python3

import sys
import time
import random
import os

DEVICE = "/dev/hidg1"
INTERVAL = 2  # seconds between movements


def to_unsigned_byte(val):
    """Convert signed integer (-127 to 127) to unsigned byte (0-255)"""
    if val < 0:
        return 256 + val
    return val


def send_mouse_report(dx, dy):
    """Send a relative mouse move (randomized x/y deltas)"""
    try:
        ux = to_unsigned_byte(dx)
        uy = to_unsigned_byte(dy)
        with open(DEVICE, 'wb') as device:
            # Send HID report: button state (0x00) + x delta + y delta
            device.write(bytes([0x00, ux, uy]))
    except IOError as e:
        print(f"Error writing to device: {e}")
        sys.exit(1)


def main():
    # Get mode from command line argument, default to 'normal'
    mode = sys.argv[1] if len(sys.argv) > 1 else 'normal'

    # Ensure the device exists
    if not os.path.exists(DEVICE):
        print(f"Error: {DEVICE} not found. Is the USB mouse gadget active?")
        sys.exit(1)

    print(f"Starting mouse jiggler in '{mode}' mode with random motion. Ctrl+C to stop.")

    try:
        while True:
            if mode == 'discrete':
                # Small random movement
                dx = random.randint(-1, 1)  # -1 to 1
                dy = random.randint(-1, 1)
                send_mouse_report(dx, dy)

            elif mode == 'normal':
                # Moderate random move out and return
                dx = random.randint(-5, 5)  # -5 to +5
                dy = random.randint(-5, 5)
                send_mouse_report(dx, dy)
                time.sleep(0.1)
                send_mouse_report(-dx, -dy)  # return to approx origin

            elif mode == 'aggressive':
                # Larger random movements
                dx = random.randint(-15, 15)  # -15 to +15
                dy = random.randint(-15, 15)
                send_mouse_report(dx, dy)

            else:
                print(f"Unknown mode: {mode}. Use: discrete, normal, or aggressive.")
                sys.exit(1)

            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\nMouse jiggler stopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()