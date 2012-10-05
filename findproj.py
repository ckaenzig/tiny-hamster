#!/usr/bin/env python

import tinylib
import tinyconf
import sys

tiny = tinylib.TinyServer(tinyconf.user_name, tinyconf.user_pwd, tinyconf.tiny_db)

print
for proj in tiny.search_account(sys.argv[1]):
  print proj[1]
print 
