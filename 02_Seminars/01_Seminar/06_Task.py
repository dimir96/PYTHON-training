a = int(input('Введите число: ')) - 1
m=a
p=1
result=0
while m>0:
    result=result+m%2*p
    p=p*10
    m=m//2

print(int(result) * 5)