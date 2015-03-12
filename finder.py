errorCodes = []
with open("errorCodesMapping.properties", "r") as ins:
  for line in ins:
    split = line.split("|")
    if len(split) > 1:
      errorCodes.append([split[1], split[2].strip("\n")])

knownErrorCodes = []
with open("errorCodeDoc.csv") as ins:
  for line in ins:
    split = line.split(",")
    if len(split) > 1:
      knownErrorCodes.append(split[1])
  
unknownErrorCodes = []
for error in errorCodes:
  if error[0] not in knownErrorCodes:
    unknownErrorCodes.append(error)

print "%s error codes found" % len(unknownErrorCodes)
for error in unknownErrorCodes:
  print error
