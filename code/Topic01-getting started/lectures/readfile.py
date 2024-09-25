# read in a simple file
# Author: Andrew Beatty

FILENAME = "data.txt"
DATADIR = "../datafiles/"

print (DATADIR + FILENAME)
with open(DATADIR + FILENAME, "rt") as fp:
    total = 0
    for line in fp:
        total += int(line)
        print (f"{line} is size {len(line)}")
    print("")
    print (f"total is {total}")