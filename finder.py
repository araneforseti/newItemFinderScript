#!/usr/bin/python

import sys

if len(sys.argv) != 3:
  print len(sys.argv)
  print sys.argv
  sys.exit("Usage: python finder.py <potentialAdditionalList> <knownItemsList>")

errorCodes = []
with open(sys.argv[1], "r") as ins:
  for line in ins:
    split = line.split("|")
    if len(split) > 1:
      errorCodes.append(split[1])

knownErrorCodes = []
with open(sys.argv[2]) as ins:
  for line in ins:
    split = line.split(",")
    if len(split) > 1:
      knownErrorCodes.append(split[1])
  
unknownErrorCodes = list(set(errorCodes) - set(knownErrorCodes))

print "%s error codes found" % len(unknownErrorCodes)
for error in unknownErrorCodes:
  print error
