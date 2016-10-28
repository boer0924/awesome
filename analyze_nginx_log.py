#!venv/bin/python
# -*- coding: utf-8 -*-
import sys
import re

line_number = 0
if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
    print "\033[1;31;40mUsage::\033[1;32;40mpython analyze_nginx_log.py 28/Apr/2016:18:20\033[0m"
    sys.exit()
else:
    log_file = '/var/log/nginx/access.log'
    with open(log_file, 'r') as f:
        for line in f.readlines():
            line_number += 1
            regular = r'\[' + sys.argv[1] + '.*?\]'
            p = re.compile(regular)
            if p.search(line):
                try:
                    pattern = re.compile(r'HTTP/1.1"(\d{0, 3})')
                    status_code = pattern.search(line).group(1)
                except Exception:
                    pass
                if status_code not in ['200', '301', '302']:
                    print line_number, ':===:', status_code, ':===:', line