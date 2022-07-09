a = float(input('Введите число: '))
if a * 10 % 10 > 0:
    print(int(a * 10 % 10))
else:
    print('нет')