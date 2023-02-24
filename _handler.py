import sys
import subprocess
import os
import _parser

_parser.parse(sys.argv[1], 'out.py')
subprocess.run('python out.py')
os.remove('out.py')