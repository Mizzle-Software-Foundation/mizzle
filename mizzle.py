<<<<<<< HEAD
import subprocess
import os
import sys

thisdir = os.path.dirname(os.path.abspath(__file__))  # the dir we run from idiot!
script = os.path.abspath(os.path.join(thisdir, "src", "parse.py"))
subprocess.run([sys.executable, script], check=True)
=======
import subprocess
import os

thisdir = os.path.dirname(os.path.abspath(__file__))  # the dir we run from idiot!
script = os.path.abspath(os.path.join(thisdir, "src", "parse.py"))
subprocess.run([sys.executable, script], check=True)
>>>>>>> 4d1d2d8deaaa3a0b5b40f94f7f631df30a1e1db3
