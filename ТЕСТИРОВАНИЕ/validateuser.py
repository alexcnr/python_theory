#!/usr/bin/env python3

def validate_user(username, minlen):
#""" роверяет, является ли выбранное имя пользователя действительным"""

    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
#если переменная minlen равна нулю или отрицательному числу

    if len(username) < minlen:
        return False
#указанное имя представляет собой как минимум 
# определенное количество символов с минимальным 
# значением
    if not username.isalnum():
#проверяем, есть ли в строке не 
# алфавитно-цифровые символы
        return False
    return True
