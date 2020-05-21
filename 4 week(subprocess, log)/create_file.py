#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]
#скрипт получает имя файла в качестве аргумента командной строки
if not os.path.exists(filename):
    #Когда файл не существует, он создает его, записывая в него строку
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

#Когда файл существует, наш скрипт выводит сообщение об ошибке 
# и завершается со значением выхода равным единице
