# 1. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('1T.txt', 'r') as file:
    li = list(map(int, file.read().split()))
    res = 0
    for x in range(1,len(li)):
        if li[x] - 1 != li[x-1]:
            res = li[x] -1
    print(res)