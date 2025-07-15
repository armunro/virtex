#!/bin/bash

DEVICE="/dev/hidg1"
MODE=${1:-normal}   # default mode = normal
INTERVAL=2          # seconds between movements

# Ensure the device exists
if [ ! -e "$DEVICE" ]; then
    echo "Error: $DEVICE not found. Is the USB mouse gadget active?"
    exit 1
fi

# Convert signed integer (-127 to 127) to unsigned byte (0–255)
to_unsigned_byte() {
    local val=$1
    if (( val < 0 )); then
        printf '%02x' $(( 256 + val ))
    else
        printf '%02x' $val
    fi
}

# Send a relative mouse move (randomized x/y deltas)
send_mouse_report() {
    local dx=$1
    local dy=$2
    local ux=$(to_unsigned_byte "$dx")
    local uy=$(to_unsigned_byte "$dy")
    printf "\\x00\\x$ux\\x$uy" > "$DEVICE"
}

echo "Starting mouse jiggler in '$MODE' mode with random motion. Ctrl+C to stop."

while true; do
    case "$MODE" in
        discrete)
            # Small random movement
            dx=$((RANDOM % 3 - 1))   # -1 to 1
            dy=$((RANDOM % 3 - 1))
            send_mouse_report "$dx" "$dy"
            ;;

        normal)
            # Moderate random move out and return
            dx=$((RANDOM % 11 - 5))  # -5 to +5
            dy=$((RANDOM % 11 - 5))
            send_mouse_report "$dx" "$dy"
            sleep 0.1
            send_mouse_report $((-dx)) $((-dy))  # return to approx origin
            ;;

        aggressive)
            # Larger random movements
            dx=$((RANDOM % 31 - 15))  # -15 to +15
            dy=$((RANDOM % 31 - 15))
            send_mouse_report "$dx" "$dy"
            ;;

        *)
            echo "Unknown mode: $MODE. Use: discrete, normal, or aggressive."
            exit 1
            ;;
    esac
    sleep "$INTERVAL"
done
