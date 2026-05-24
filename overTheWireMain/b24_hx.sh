#!/bin/bash
# in linux's world, extensions mean nothing, as long as permitted allow, system gonna trying to run it, no matter a .jpg or .py
# #!/usr/bin/python3 to run as python
cat /etc/bandit_pass/bandit24 > /tmp/psw.txt
# foget not to chmod 777 psw.txt to allow others write in
# also the chmod +x hx.sh to add execution permit
# this is better than chmod 711 to modify more
# chmod ugo +x == chmod a+x == chmod +x
