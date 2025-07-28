<<<<<<< HEAD
import sys
import json
import os

temp_file_path = sys.argv[1]
out_file_path = sys.argv[2].replace(".mz", ".py")

# Load the command list from the file
with open(temp_file_path, "r") as file1:
    commands_to_compile = json.load(file1)

# yeah, yeah let me do it.
file = out_file_path

with open(file, "w") as f:
    for line in commands_to_compile:
        f.write(line + "\n")

print("Compilation complete! The file has been written to:", file)

os.remove(temp_file_path)

os._exit(0)
=======
import os
import parse
import importlib.util
thisdir = os.path.dirname(os.path.abspath(__file__)) # the dir we run from idiot!
mizzle_py_path = os.path.abspath(os.path.join(thisdir, "..", "mizzle.py"))
spec = importlib.util.spec_from_file_location("mizzle", mizzle_py_path)
mizzle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mizzle)

# yeah, yeah let me do it.
commands_to_compile = parse.parsed_commands()
file = parse.mz_file()

with open(file, "w") as f:
    for line in commands_to_compile:
        f.write(line + "\n")
>>>>>>> 4d1d2d8deaaa3a0b5b40f94f7f631df30a1e1db3
