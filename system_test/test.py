#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    """функция получит удаленную проверку и вернет true, 
    если более чем на 20 процентов свободно или false, если меньше."""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    """роверим использование в течение целой секунды. Мы скажем, что машина исправна, 
     cpu_usage составляет менее 75 процентов"""
    usage = psutil.cpu_percent(1)
    return usage < 75
#добавим основную часть нашего скрипта, где мы проверим, возвращает ли одна из этих двух функций false

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR")
else:
    print("EVERYTHING IS OK!!!")

