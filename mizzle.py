import subprocess
import os
import sys

thisdir = os.path.dirname(os.path.abspath(__file__))  # the dir we run from idiot!
script = os.path.abspath(os.path.join(thisdir, "src", "parse.py"))
subprocess.run([sys.executable, script], check=True)