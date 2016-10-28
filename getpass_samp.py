#!../venv/bin/python
# -*- coding: utf-8 -*-

import getpass

user = raw_input('Please input your name.\nName:')
print 'Please input', user + '\'s password.'
passwd = getpass.getpass()

print 'Please confirm', user + '\'s password.'
if getpass.getpass() == passwd:
    print '\nHello:', user, '\tPassword:', passwd
else:
    print '\nInvaild username or password'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          