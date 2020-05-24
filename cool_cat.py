import time
import sys

with open(sys.argv[1]) as file:
    lines = file.readlines()
    for line in lines:
        for c in list(line):
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.008)
