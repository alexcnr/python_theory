#!/usr/bin/env python3
#три строки, каждая из которых взаимодействует с различным потоком. 
# В первом мы читаем из стандартного ввода, 
# во втором мы пишем в стандартный вывод. 
# В последнем случае мы генерируем ошибку, 
# объединяя строку в целое число

data  = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)
