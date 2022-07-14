# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def sum_multipl(list):
    count_start = 0
    count_end = -1
    suma = []
    while count_start < len(list) // 2:
        suma.append(list[count_start] * list[count_end])
        count_start += 1
        count_end -= 1
    if len(list) % 2 == 1:
        suma.append(list[len(list) // 2] ** 2)
    return suma

a = [2, 3, 4, 5, 6]
b = [2, 3, 5, 6]

print(sum_multipl(a))
print(sum_multipl(b))