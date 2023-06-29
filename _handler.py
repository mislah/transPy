import sys
import subprocess
import _parser
import tempfile
import os

cmd = sys.argv[1]
ifile = sys.argv[2]

ofile = None
if len(sys.argv) == 5:
    ofile = sys.argv[4]

if sys.argv[3] == "CMPLONLY": # Compile only
    if not ofile:
        ofile = os.path.splitext(ifile)[0] + "_.py"
    _parser.parse(ifile, ofile)
elif sys.argv[3] == "CMPLNRUN": # Compile and run
    if not ofile:
        ofile = tempfile.NamedTemporaryFile().name
    _parser.parse(ifile, ofile)
    subprocess.run((cmd, ofile))