#!/usr/bin/env python3

import re

def rearrange_name(name):
    """FINAL VERSION"""
    result = re.search(r"^([\w\ .-]*), ([\w\ .-]*)$", name)
    if result is None:
        return name
    #Если результат отсутствует, это означает, что он не соответствует формату
    #Так что в этом случае он просто вернет имя как есть.
    return "{} {}".format(result[2], result[1])

#print(rearrange_name("Lovelace, Ada"))
#print(rearrange_name("Richie, Dennis"))
#print(rearrange_name("Hopper, Grace M."))