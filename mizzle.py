import subprocess
import os

compiledir = os.path.dirname(os.path.abspath(__file__))
script = os.path.abspath(os.path.join(this_dir, "src", "parse.py"))
subprocess.run([sys.executable, script], check=True)
