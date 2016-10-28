#!venv/bin/python
# -*- coding: utf-8 -*-

import time

def follow(thefile):     
    thefile.seek(0, 2)
    while 1:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue         
        yield line

with open('/var/log/nginx/access.log', 'r') as thefile:
    for line in follow(thefile):
        print(line)