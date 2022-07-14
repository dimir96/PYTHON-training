# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def to_decimal(number):
    decimal_number = ''
    y = number
    while y > 0:
        decimal_number = decimal_number + str(y % 2)
        y = int(y // 2)
    return decimal_number[::-1]


a = 45  # 101101
b = 3   # 11
c = 2   # 10

print(to_decimal(a))
print(to_decimal(b))
print(to_decimal(c))