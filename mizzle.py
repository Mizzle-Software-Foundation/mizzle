import subprocess
import os

thisdir = os.path.dirname(os.path.abspath(__file__))  # the dir we run from idiot!
script = os.path.abspath(os.path.join(this_dir, "src", "parse.py"))
subprocess.run([sys.executable, script], check=True)
