# 35(Доп). Даны два файла, в каждом из которых находится
# запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

first = open("first.txt", "r")
first = first.read().split(' + ')
second = open("second.txt", "r")
second = second.read().split(' + ')

newfirst = []
for i in first:
    newfirst.append(i.split('x^'))

newsecond = []
for i in second:
    newsecond.append(i.split('x^'))

result = []
for i in newfirst:
    for j in newsecond:
        if len(i) > 1:
            if i[-1] == j[-1]:
                result.append([int(i[0]) + int(j[0]), int(i[-1])])
        if len(i) == 1:
            if len(j) == 1:
                result.append(int(i[0]) + int(j[0]))

f = open('result.txt', 'w')
f.write(str(result))
f.close()

f = open("result.txt", "r")
print(f.read())
