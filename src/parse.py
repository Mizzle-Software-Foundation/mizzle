import os
import json
# there is gonna be a lot of parsing, becuase of the massive amount of syntax to be added.
commands = []
current_command = []
parsed_commands = []
parsed_command = []
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
builtins = os.path.abspath(os.path.join(thisdir, "syntaxrule.json"))
with open(builtins, "r") as syntaxfile:
  syntax = json.load(syntaxfile)
