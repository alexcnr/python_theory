#!/usr/bin/env python3

import os
import sys
import re

logfile = sys.argv[1] #аргумент командной строки для пути к файлу журнала
processes = {}
returned_errors = []
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
    #игнорировать любую строку без подстроки Cron
        pattern = r"([A-Za-z0-9:\-\ ]*)([A-Z]{4,})([\[[0-9]{1,5}[\]])([: \(\)A-Za-z\/\-&\.!\[\];]*)"
        #([\[[0-9]{1,5}[\]])      -  3 group [8476]
        #([A-Za-z0-9:\-\ ]*)     -  1 group  May 21 09:17:01 alexczn-desktop CRON
        #([: \(\)A-Za-z\/\-&\.!\[\];]*)   -   4 group  to end
        # ([A-Z]{4,})    -  2 group    CRON

        result = re.search(pattern, line)
        for i in line:
            rez = re.sub(pattern, r"process name - \2  and number \3 , has description - \4", line)
            if rez not in returned_errors:
                returned_errors.append(rez)
        if result is None:
            continue
        name = result[2]
        processes[name] = processes.get(name, 0) + 1
        #print(result[2])  - TypeError: 'NoneType' object is not subscriptable
        #print(result[1])  # OK
       

        #print(line.strip())
print(processes) #дает процессы и их количество в логе
print(returned_errors)

def file_output(returned_errors):
    with open("lo.log", "w") as file:
        for error in returned_errors:
            file.write(error)

file_output(returned_errors)

#pattern = r"USER \((\w+)\)$"
#pattern = r"([a-z\-]*)([\[[0-9]{1,5}[\]])"
# line = "May 21 08:49:34 alexczn-desktop gnome-shell[5177]: # _g_io_module_get_default: Found default implementation gvfs (GDaemonVfs) for ‘gio-vfs’"

#May 21 09:17:01 alexczn-desktop CRON[8476]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
#May 21 08:39:01 alexczn-desktop CRON[4033]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)



