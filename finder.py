#!/usr/bin/python

import sys

def create_list_from_file(file, separator):
  new_list = []
  with open(file, "r") as ins:
    for line in ins:
      split = line.split(separator)
      if len(split) > 1:
        new_list.append(split[1])
  return new_list

if len(sys.argv) != 3:
  print len(sys.argv)
  print sys.argv
  sys.exit("Usage: python finder.py <potentialAdditionalList> <knownItemsList>")

errorCodes = create_list_from_file(sys.argv[1], "|")

knownErrorCodes = create_list_from_file(sys.argv[2], ",")
  
unknownErrorCodes = list(set(errorCodes) - set(knownErrorCodes))

print "%s new items found" % len(unknownErrorCodes)
for error in unknownErrorCodes:
  print error
