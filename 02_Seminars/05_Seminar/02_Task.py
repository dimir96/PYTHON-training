# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
#
# *Пример:*
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

li = [1, 5, 2, 3, 4, 6, 1, 7]

n_li =[li[0]]

print(n_li)
for x in range(len(li)):
    if li[x] > n_li[-1]:
        n_li.append(li[x])
print(n_li)
# 1:17:50