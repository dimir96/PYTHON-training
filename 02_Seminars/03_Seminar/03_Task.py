a = ['23', '323', '24', '23', '34323']
ssearch = '23'

count = 0

for i in a:
    if i == search:
        count += 1
    if count == 2:
        print(a.index(i))
        break
    if count < 2:
        print('NO')