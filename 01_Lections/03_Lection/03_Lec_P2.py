# # # list = []
# # #
# # # for i in range(1, 101):
# # #     if(i%2 == 0):
# # #         list.append(i)
# # #
# #
# # def f(x):
# #     return x**3
# #
# # list  = [(i, f(i)) for i in range(1,21) if i%2 == 0]
# # print(list)
# #
# #
#
# print(*[(i, i ** 2) for i in [1, 2, 3, 5, 8, 15, 23, 38] if i%2 == 0])

# li = [x for x in range(1,10)]
# li = list(map(lambda x: x+10, li))
#
# print(li)
#
# data = list(map(int, '1 2 3 4 5 6'.split()))
# print(data)

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))

print(res)