#!/usr/bin/env python

import tinylib
import sys
import getpass
import common

try:
  proj_arg = sys.argv[1]
except IndexError:
  print "usage: findproj.py <project>"
  sys.exit(1)


tinyconf = common.build_config()

tiny = tinylib.TinyServer(tinyconf.user_name, tinyconf.user_pwd, tinyconf.tiny_db, tinyconf.rpc_url)

print
for proj in tiny.search_project(proj_arg, timesheetable_only=True):
  print proj[1]
print
