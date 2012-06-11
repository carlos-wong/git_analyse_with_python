#!/usr/bin/python
import os
import sys
import time
import string
import commands

time_pos = 1

def run_sys_command(command):
  status,output_file = commands.getstatusoutput(command.strip())
  print "\"%s\" return: "%(command.strip()),"status: ", status
  if(status != 0):
    print command.strip(),"return error!!! we only do to is exit"
    sys.exit()
  return output_file

i = 0
for path in sys.argv:
  i = 1+i
if i != 3:
  print "./git_analyse.py who path"
else:
  i = 0
  who = sys.argv[1]
  work_path = sys.argv[2]
  os.chdir(work_path)
  get_git_command = "git log --author=\"%s\" --pretty=format:\"%%ci\""%(who)
  analyse_data = run_sys_command(get_git_command)
  array_anlayse = analyse_data.split("\n")
  for enum_analyse in array_anlayse:
    print enum_analyse
    print time.strptime(enum_analyse,"%Y-%m-%d %H:%M:%S +0800").tm_hour

