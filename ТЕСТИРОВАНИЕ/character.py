#!/usr/bin/env python3

def character_frequency(filename):
    
    """читает содержимое файла, чтобы посчитать частоту каждого символа """
    try:
        f = open(filename)
    except OSError:
        return None


    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters
