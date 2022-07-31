

# Пам-парам парам-пам парам


string_input = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

string_input = string_input.split()

keys = [x.count('a') for x in string_input]

if keys.count(keys[0]) == len(keys):
    print('Парам пам-пам')
else:
    print('Пам парам')