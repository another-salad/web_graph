"""Constants and imports"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(__file__, "../")))


SENSOR_NAMES = ['server_room', 'cats_room', 'office']

#
# ----- Docker secret file names -----
#
UN = "un"
PW = "pw"
HOST = "host"

# DB
ACCESS_TOKEN_KEY = "access_token"
