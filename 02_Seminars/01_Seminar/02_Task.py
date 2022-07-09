# a = int(input('Введите число:'))
# b = int(input('Введите число:'))
# c = int(input('Введите число:'))
# d = int(input('Введите число:'))
# e = int(input('Введите число:'))
# max = a
# if max < b:
#     max = b
# if max < c:
#     max = c
# if max < d:
#     max = d
# if max < e:
#     max = e
# print(max)


a = list(map(int, input('Введите пять чисел через пробел:').split()))
max_number = a[0]
print(a)
for i in a:
    if i > max_number:
        max_number = i

print(max_number)