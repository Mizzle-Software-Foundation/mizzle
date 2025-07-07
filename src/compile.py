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
compileto = mizzle.compiledir()
filename = None # imma add this bro, i need to add the parser and stuff tho.

fileoutput = f"{compileto}{filename}"

with open(fileoutput, "w") as f:
    for line in commands_to_compile:
        f.write(line + "\n")
