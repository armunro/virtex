# Virtex Bitwarden
Virtex can simplify logins and authentication by storing references to Bitwarden items. Once a reference is captured in a `*.bwref.yaml` file, they can be used with the

## Setup
Put your Bitwarden master password in a `~/virtex/vpm/keys/bw/master.bwpass.txt`

## Bitwarden Reference Format
Bitwarden references are stored in `~/virtex/vpm/keys/bw-refs`. The file structure is as follows.
```yaml
id: a546c86b-5a1e-470d-a118-b2330114d371
template: "{username}\t{password}\n"
```
- The file extension must be `.bwref.yaml`
- The `template` property enables customization of how the item contets are sent to the Virtual Keyboard.
- `{username}` and `{password}` tokens are replaced when the text is injected.

## Creating Bitwarden References (vtx-bwref)
The `vtx-bwref` command quickly locates an item in bitwarden and creates a `.bwref.yaml` file in the refs directory.
```bash
vtx-bwref virtex
# Searching Bitwarden for 'virtex': : 6step [00:18,  3.13s/step]
# Select an item:
#
#* {'id': '11111111-1111-1111-1111-111111111111', 'name': 'Virtex Key'}
#  {'id': '22222222-2222-2222-2222-222222222222', 'name': 'Virtex Test Secret'}
# Enter name: twarden for 'virtex': : 6step [00:17,  2.91s/step]
# virtex-test-ref
```

## Push Bitwarden Item (vtx-bw)
The `vtx-bw` command lists all `.bwref.yaml` files stored and provides a simple selection list. Pressing `[Enter]` will start the process of getting the item, and sending it to the Virtual Keyboard.
```bash
vtx-bw
# Select Bitwarden Item:
# 
# * virtex-test-ref.bwref.yaml
```