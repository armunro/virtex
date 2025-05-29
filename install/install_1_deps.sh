  #!/usr/bin/bash

/boot/dietpi/dietpi-software install 9     # node
/boot/dietpi/dietpi-software install 17    # git
/boot/dietpi/dietpi-software install 130   # python

pip install pyyaml --root-user-action=ignore
pip install pick --root-user-action=ignore
pip install colorama --root-user-action=ignore
pip install tqdm --root-user-action=ignore
pip install python-dotenv --root-user-action=ignore
pip install flask --root-user-action=ignore
pip install alive_progress --root-user-action=ignore
