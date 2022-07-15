#!/usr/bin/python3

# vpn_init.py

import os, time
import re

XSRV_FILE = '/usr/bin/xvfb-run'
XSRV_PS = 'xvfb-run'
OPERA_CMD = XSRV_FILE + ' /usr/local/opera-beta/opera-beta --no-sandbox'
OPERA_PS = 'opera-beta'
TIMEOUT = 30
PROFILE_DIR = os.getenv('HOME') + '/.config/opera-beta'
PREF_FILE = PROFILE_DIR + '/Preferences'
S_FROM='"freedom":{[^}]+}'
S_TO='"freedom":{"proxy_switcher":{"bytes_transferred":"0","country_code":"EU","enabled":true,"forbidden":false,"ui_visible":true}'

# create config
os.system(OPERA_CMD + ' & ')
time.sleep(TIMEOUT)
os.system('killall ' + OPERA_PS)
time.sleep(TIMEOUT)
# in config: turn vpn on
with open(PREF_FILE, 'r+') as pref_file:
    try:
        prefs = pref_file.readline()
        pref_file.seek(0)
        pref_file.write(re.sub(S_FROM, S_TO, prefs))
        pref_file.trancate()
    except:
        pass
time.sleep(TIMEOUT)

