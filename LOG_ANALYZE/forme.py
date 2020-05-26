#!/usr/bin/env python3


import re
import csv
import operator
import sys


#user_statistics.html
#error_message.html

logfile = sys.argv[1] #аргумент командной строки для пути к файлу журнала
#тестовые выражения журнала для написания регул.выражения:
#May 21 11:26:14 alexczn-desktop gnome-shell[1316]: Unset XDG_SESSION_ID, getCurrentSessionProxy() called outside a user session. Asking logind directly.
#May 21 11:26:14 alexczn-desktop gnome-shell[1316]: Will monitor session c1
#May 21 11:26:14 alexczn-desktop dbus-daemon[583]: [system] Activating via systemd: service name='org.freedesktop.locale1' unit='dbus-org.freedesktop.locale1.service' requested by ':1.47' (uid=124 pid=1316 comm="/usr/bin/gnome-shell " label="unconfined")

pattern = r"([a-z\-]*\[[0-9]{1,5}[\]])([:\ \(\)\)A-Za-z1-9\/_,\-&\.!\[\];=\'\"]*)"

# ([:\ \(\)\)A-Za-z1-9\/_,\-&\.!\[\];=\'\"]*)      - 2 group   - to end...
#([a-z\-]*\[[0-9]{1,5}[\]])   -   1 group    -    name of process, +   example - [1316]

errors = { }

#logfile = 'syslog.log'
f = open(logfile, 'r')

errorfile = 'error_message.csv'
#вариант через sub новое выражение и его как ключ

for log in f:
    result = re.search(pattern, log)
    if result != None:
        if result.group(1) not in errors.keys():
            errors[result.group(1)] = 0
        errors[result.group(1)] += 1
        

errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)


f.close()
errors.insert(0, ('Errors', 'Count'))

f = open(errorfile, 'w')
for error in errors:
    a, b = error
    f.write(str(a)+','+str(b)+"\n")
f.close()



