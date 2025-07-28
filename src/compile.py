
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