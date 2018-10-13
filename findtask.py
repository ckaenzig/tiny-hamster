#!/usr/bin/env python

import tinylib
import tinyconf
import sys
import common

try:
  proj_arg = sys.argv[1]
  task_arg = sys.argv[2]
except IndexError:
  print "usage: findproj.py <project> <task>"
  sys.exit(1)

tinyconf = common.build_config()

tiny = tinylib.TinyServer(tinyconf.user_name, tinyconf.user_pwd, tinyconf.tiny_db, tinyconf.rpc_url)

print
for proj in tiny.search_account(proj_arg):
  print "%s:" %(proj[1])
  for task in tiny.search_task(proj[0], task_arg):
    print "  %s" %(task[1])
print 
