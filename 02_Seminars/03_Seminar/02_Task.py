# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

a = ['23', '323', '24']
search = 23

for i in a:
    if int(i) == search:
        print('DA')
    else:
        print('NET')