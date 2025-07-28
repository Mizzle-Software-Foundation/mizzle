import os
import json
import subprocess
import sys
# there is gonna be a lot of parsing, becuase of the massive amount of syntax to be added.
commands = []
parsed_commands = []
parsed_command = None
mz_file = input("Enter the path to your .mz file: ")
if os.path.exists(mz_file):
  pass
else:
  while True:
    mz_file = input("Enter the path to your .mz file: ")
    if os.path.exists(mz_file):
      break
    else:
      continue

# really this is a lexer, but the rest is a parser so whatever.
thisdir = os.path.dirname(os.path.abspath(__file__))  # the dir we run from idiot!
compile_script = os.path.abspath(os.path.join(thisdir, "compile.py"))
builtins = os.path.abspath(os.path.join(thisdir, "syntaxrule.json"))
with open(builtins, "r") as syntaxfile:
  syntax = json.load(syntaxfile)

# we are parsing the file line by line now! then checking for commands, and outputting the command in - PYTHON - !!!!!
with open(mz_file, "r") as mzfile:
  for line in mzfile:
    line = line.strip()
    for cmd in syntax:
      cmd_name = cmd["name"].rstrip("();")
      cmd_value = cmd["value"].rstrip("()")

      if line.startswith(cmd_name):
        parsed_command = line.replace(cmd_name, cmd_value, 1)
        parsed_command = parsed_command[:-1] # no more semicolon BLEH!
        parsed_commands.append(parsed_command)
        break

  temp_file_path = "temp_commands.json"

  with open(temp_file_path, "w") as f:
    json.dump(parsed_commands, f)
  
  subprocess.run([sys.executable, compile_script, temp_file_path, mz_file], check=True)