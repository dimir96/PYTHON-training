# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти: '))

if a == 1:
    print('х - от нуля до плюс бесконечности')
    print('у - от нуля до плюс бесконечности')
if a == 2:
    print('х - от нуля до плюс бесконечности')
    print('у - от минус бесконечности до нуля')
if a == 3:
    print('х - от минус бесконечности до нуля')
    print('у - от минус бесконечности до нуля')
if a == 4:
    print('х - от минус бесконечности до нуля')
    print('у - от нуля до плюс бесконечности')