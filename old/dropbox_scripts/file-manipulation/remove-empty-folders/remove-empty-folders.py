#! /usr/bin/python3
import os

for dirpath, dirnames, files in os.walk('.'):
  if not (files or dirnames):
    print('removing: ' + dirpath)
    os.rmdir(dirpath)