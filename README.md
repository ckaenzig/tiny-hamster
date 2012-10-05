tiny-hamster
============

Import entries from the Hamster time tracker to an OpenERP timesheet

This is custom made for our OpenERP setup at Camptocamp and is probably quite
specific (I'm not sure).

Installation
------------

1. Checkout this repository somewhere on your system, and symlink the commands
(tinyham.py, findproj.py) in your ~/bin or something in your  $PATH.
2. Created a tinyconf.py file based on tinyconf.py.example with your username,
password, and the openerp database to use.

Usage
-----

Use the Hamster time tracker[1] to track what you're doing. A task's category
must match a project in OpenERP, and the task's tag (optional) can be set to
specify a task in OpenERP (the category can be specified using an '@' sign in
the task's description).

[1] https://github.com/projecthamster/hamster

At the end of the day, use the tinyham.py command (without argument) to import
the current day's tasks into OpenERP. tinyham will any error it finds and ask
you to fix them. You can also import another day's work by adding the date as
argument (format YYYY-MM-DD).

Typical workflow
----------------

tiny-hamster has a limitation in that it cannot create timesheet objects in
OpenERP (weekly sheets). So you first have to create and save them once in
OpenERP. So here is the workflow I recommend (and personnaly use) :

1. All week long, use Hamster to track your time without worrying about
OpenERP.
2. On Monday morning, open and log into OpenERP, open the current timesheet
(that of the new week) which will create it if necessary, and save it empty.
3. Use tiny-hamster to import all days of the past week into OpenERP.
4. In OpenERP, check to total time of the past week and confirm it.

That's it. You can also import data into OpenERP more frequently (especially
recommended near the end of the month to help the administrative team).

