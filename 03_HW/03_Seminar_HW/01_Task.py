# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def multiply_odd(list):
    result = 0
    count =1
    while count < len(list):
        result += list[count]
        count += 2
    return result


a = [2, 3, 5, 9, 3]

print(multiply_odd(a))