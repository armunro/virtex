# VTEXT2 Format

VTEXT2 is an extended scripting language for Virtex devices. It keeps the YAML
style of the original `.vtext` files while adding more powerful constructs for
automation of keyboard and mouse input.

## Basic Structure
A script is a YAML document containing a `steps` list. Each entry represents a
command. The command name is the key and its argument may be a scalar or a
nested mapping.

```yaml
steps:
  - launch: notepad
  - wait: 1
  - text: "Hello world"
  - hotkey: CTRL+S
  - text: "notes.txt\n"
```

## Supported Commands
* `launch`: open an application using the run dialog.
* `text`: type arbitrary text. Supports an optional `interval` argument for per
  character delay.
* `hotkey`: send a key combination such as `CTRL+ALT+DEL`.
* `mouse.move`: relative mouse movement with `x` and `y` values.
* `mouse.click`: mouse click (`left`, `right` or `middle`).
* `mouse.scroll`: scroll the wheel by an integer amount.
* `wait`: pause execution for a number of seconds.
* `repeat`: run a nested list of steps multiple times.

Example of `repeat`:
```yaml
steps:
  - repeat:
      times: 3
      steps:
        - text: Spam
        - wait: 0.5
```

These primitives allow complex automation scenarios while keeping the format
human readable.
