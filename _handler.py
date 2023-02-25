import sys
import subprocess
import os
import _parser

TMP = 'out.py'

_parser.parse(sys.argv[1], TMP)
subprocess.run((sys.argv[2], TMP))
os.remove(TMP)