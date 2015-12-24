__author__ = 'MFlores1'

import struct
import sys

from ps2_verify_movement27 import testRobotMovement

with open('ps2_verify_movement27.pyc', 'rb') as f:
    print struct.unpack('<H', f.read(2))

print sys.version