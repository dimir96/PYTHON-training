a = int(input('Введите число: '))
if (a % 10 == 0 or a % 15 == 0) and not a % 30 == 0:
    print('ДА')
else:
    print('НЕТ')