a = int(input('Введите количество элементов словаря: '))
dictionary = {}
x=1
for i in range(1, a + 1):
    dictionary[i] = 3 * i + 1
print(dictionary)
