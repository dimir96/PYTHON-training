# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = True
y = False
z = True
if not (x or y or z) == (not (x) and not (y) and not (z)):
    print('Справедливо')
else:
    print ('Не справедливо')