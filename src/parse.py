import os
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
# no i have no idea when i am gonna keep making this.
