# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
# 5! = 120

a = int(input('Введите число: '))
x = 1
for i in range (1, a+1):
    x *= i
print(x)