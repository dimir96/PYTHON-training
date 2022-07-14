# *5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def niegafibonacci(number):
    count = number
    nefative_fibonacci = [1, -1]
    positive_fibonacci = [1, 1]
    while count - 2 > 0:
        nefative_fibonacci.append(nefative_fibonacci[-2] - nefative_fibonacci[-1])
        count -= 1
    while count < number:
        positive_fibonacci.append(positive_fibonacci[-1] + positive_fibonacci[-2])
        count += 1
    return nefative_fibonacci[::-1] + [0] + positive_fibonacci

a = 8

print(niegafibonacci(a))