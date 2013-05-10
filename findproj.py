#!/usr/bin/env python

import tinylib
import tinyconf
import sys

try:
  proj_arg = sys.argv[1]
except IndexError:
  print "usage: findproj.py <project>"
  sys.exit(1)


tiny = tinylib.TinyServer(tinyconf.user_name, tinyconf.user_pwd, tinyconf.tiny_db, tinyconf.rpc_url)

print
for proj in tiny.search_account(proj_arg):
  print proj[1]
print 
