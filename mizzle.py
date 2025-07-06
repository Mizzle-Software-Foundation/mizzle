import subprocess
import os

script = os.path.abspath(os.path.join(this_dir, "src", "compile.py"))
subprocess.run([sys.executable, script], check=True)
