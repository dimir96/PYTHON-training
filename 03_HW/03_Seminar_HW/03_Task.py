# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



def sum_ost(list):
    new_list = []
    for i in list:
        if round(i - int(i),2) > 0:
            new_list.append(round(i - int(i), 2))
    return max(new_list) - min(new_list)

a = [1.1, 1.2, 3.1, 5, 10.01]

print(sum_ost(a))