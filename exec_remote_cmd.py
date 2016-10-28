#!venv/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import paramiko

def connect_host(host):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host)

    # Put the analyze nginx log file py script.
    ftp = client.open_sftp()
    remote_f = '/tmp/analyze_nginx_log.py'
    local_f = './analyze_nginx_log.py'
    ftp.put(local_f, remote_f)
    ftp.close()

    # Exec remote cmd
    cmd = 'python' + 'remote_f' + sys.argv[1]
    stdin, stdout, stderr = client.exec_command(cmd)
    for result in stdout.readlines():
        return result

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
        print "\033[1;31;40mUsage::\033[1;32;40mpython exec_remote_cmd.py 28/Apr/2016:18:20\033[0m"
        sys.exit()
    else:
        with open('./hosts', 'r') as f:
            for host in f.readlines():
                print connect_host(host)