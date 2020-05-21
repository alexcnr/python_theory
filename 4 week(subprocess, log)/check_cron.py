#!/usr/bin/env python3

import os
import sys
import re

logfile = sys.argv[1] #аргумент командной строки для пути к файлу журнала
usernames = {}
with open(logfile) as f:
    for line in f:
        if "May" not in line:
            continue
    #игнорировать любую строку без подстроки Cron
        pattern = r"([a-z\-]*)([\[[0-9]{1,5}[\]])" #change!!!!!
        #pattern = r"([a-z\-]*)([\[2514[\]])"#  uncorrect!!!!!!!!
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
        #print(result[2])  - TypeError: 'NoneType' object is not subscriptable
        #print(result[1])  # OK

        #print(line.strip())
print(usernames) #сейчас дает процессы и их количество в логе
#pattern = r"USER \((\w+)\)$"
#pattern = r"([a-z\-]*)([\[[0-9]{1,5}[\]])"
# line = "May 21 08:49:34 alexczn-desktop gnome-shell[5177]: # _g_io_module_get_default: Found default implementation gvfs (GDaemonVfs) for ‘gio-vfs’"


#ЦЕЛЬ - ПРОВЕРИТЬ РЕГУЛ ВЫРАЖЕНИЕ!
