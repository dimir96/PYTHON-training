# def f(x):
#     return x ** 2
# g = f
# print(f(2))
# print(g(2))



def calc(x):
    return x + 10
# print(calc(10))


def calc2(x):
    return x * 10
# print(calc2(10))


def mach(op, x):
    print(op(x))

# mach(calc, 10)


# def sum(x, y):
#     return x + y

# sum = lambda x, y: x+y

def mult(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(lambda x, y: x+y, 50, 5)



