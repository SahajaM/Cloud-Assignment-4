#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = re.sub(r'".*"',' ',line)
    # split the line into words
    words = line.split(",")
    # increase counters
    counter = 0
    if words[0] != "DATE":
        for word in words:
                counter = counter+1                
                if word:
                        if counter >= 25:
                                print '%s\t%s' % (word, 1)
