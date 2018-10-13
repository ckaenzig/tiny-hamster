import sys
import getpass
try:
    import tinyconf
except ImportError:
    print ("No configuration file found. You have to copy "
           "'tinyconf.py.example' to 'tinyconf.py' and change the options.")
    exit(1)

def build_config():
  if not hasattr(tinyconf, "user_pwd"):
    try:
      password = getpass.getpass("Odoo password: ")
    except Exception as error:
      print "Failed to get password: %s" % error
    else:
      tinyconf.user_pwd = password
  return tinyconf
