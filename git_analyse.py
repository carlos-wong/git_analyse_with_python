#!/usr/bin/python
import os
import sys
import time
import string
import commands

time_pos = 1
time_of_hour = [0,0,0,0,0,0,0,0]
time_step = 3

def run_sys_command(command):
  status,output_file = commands.getstatusoutput(command.strip())
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
  get_git_command = "git log --all --author=\"%s\" --pretty=format:\"%%ci\""%(who)
  analyse_data = run_sys_command(get_git_command)
  array_anlayse = analyse_data.split("\n")
  i = 0
  for enum_time_of_hour in time_of_hour:
    enum_time_of_hour = 0
  for enum_analyse in array_anlayse:
    time_hour = time.strptime(enum_analyse,"%Y-%m-%d %H:%M:%S +0800").tm_hour
    time_start = 0
    i = 0
    while time_hour > time_start:
      time_start = time_start+time_step
      i = i + 1
    time_of_hour[i-1] = time_of_hour[i-1]+1
  i = 0
  for enum_time_of_hour in time_of_hour:
    print "sect %d-%d is "%(i*time_step,(i+1)*time_step),enum_time_of_hour
    i = i + 1

