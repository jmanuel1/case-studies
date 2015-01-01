# Script to replace ((patterns)) with certain things.

import os, sys
from itertools import count

def parseConfig(config=None):
    files, patterns, p = [], [], False
    with open(config or "fileReplace") as f:
        for line in f:
            if line.strip() == "":
                p = True
                print("Blank line: begin pattern section")
            elif p:
                pattern = line.split()
                patterns.append(pattern)
                print("Pattern: ((" + pattern[0] + ")) get replaced with '" + pattern[1] + "'")
            else:
                file = line.strip()
                files.append(file)
                print("File: " + file)
            
    return (files, patterns)

config = None
if len(sys.argv) == 2:
    config = sys.argv[1]
    
files, patterns = parseConfig(config)
BLOCKSIZE = 512
TMP = "fileReplace.tmp"

# for each file
for file in files:
    with open(file) as f, open(TMP, "w") as t:
        lineno = count(1)
        for line in f:
            line_ = line
            for pattern in patterns:
                p = "((" + pattern[0] + "))"
                if p in line_:
                    print("Replacement of " + p + "made on line " + str(next(lineno)))
                line_ = line_.replace(p, pattern[1])
            t.write(line_)
    with open(file, "w") as f, open(TMP) as t:
        while True:
            o = t.read(BLOCKSIZE)
            if len(o) == 0:
                break
            f.write(o)
            
# leave directory clean
os.remove(TMP)