def factorial(a):
    x = 1
    for i in range(a):
        x = x * i
    return x


n = int(input('Введите число: '))
k = 2
print(int(factorial(n+k-1)/(factorial(k)*factorial(n+k-1-k))))





