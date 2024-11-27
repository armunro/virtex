# Virtext Script Automation (vtx-vtxt)
Executes virtext scripts 

## Usage

## Sample Virtext
```plainext
notepad: 1
sleep: 1
print: hello what is up
```

## Commands
- print: - Sends text after the `:` to the VKB  
- winrun - Opens the Windows run dialog
- winstart - Opens the Windows Start bar
- notepad - Opens notepad
- sleep - Add delays for UI readiness.
- enter - Press the enter key
- key - Press any key in HID.CODE.*


## Running a VirText Script

```bash
vtx-vtxt ~/virtext/vhid/vtxt/test.vtxt
```