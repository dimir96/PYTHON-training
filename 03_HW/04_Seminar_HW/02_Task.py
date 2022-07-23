# Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. (1 - составное число)


a = int(input('Введите число: '))
flag = True
list = []
for i in range(2, a+1):
    count = 2
    flag = True
    while count < i:
        if i % count == 0:
            flag = False
            break
        count += 1
    if flag == True:
        list.append(i)

print(*list)