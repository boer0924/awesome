#!/usr/bin/env python

import fileinput

for line in fileinput.input():
    print line.strip(), '\t\t', fileinput.filelineno(), '\t\t', fileinput.filename()
