# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


a = '1 23 45 43 45 23'
b = list(map(int, a.split(' ')))

print(max(b))
print(min(b))