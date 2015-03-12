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

potentialItems = create_list_from_file(sys.argv[1], "|")

knownItems = create_list_from_file(sys.argv[2], ",")
  
newItems = list(set(potentialItems) - set(knownItems))

print "%s new items found" % len(newItems)
for item in newItems:
  print item
