# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
a = int(input('Введите натуральную степень многочлена: '))
result = ''
while a >= 0:
    kef = random.randrange(0, 101)
    if kef != 0:
        if a > 0:
            result = result + str(kef) + 'x^' + str(a)
            result += ' + '
        if a == 0:
            result += str(kef)
    a -= 1


print(result)