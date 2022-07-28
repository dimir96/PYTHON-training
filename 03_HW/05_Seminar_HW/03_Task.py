# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def archive(string):
    result = ''
    i = 0
    count_symbols = 0
    while i < len(string)-1:
        if string[i] != string[i + 1]:
            result += string[i]
        if i+1 == len(string)-1 and string[i] != string[i + 1]:
            result += string[i+1]
        while string[i] == string[i + 1]:
            count_symbols += 1
            i += 1
        if count_symbols > 4:
            result += '#'
            result += chr(count_symbols)
            result += string[i]
        if 0 < count_symbols < 4:
            for j in range(count_symbols + 1):
                result += string[i]
        count_symbols = 0
        i += 1
        if count_symbols == 0:
            continue
    return result


def unpack(string):
    result = ''
    i = 0
    while i < len(string):
        if string[i] != "#":
            result += string[i]
        if string[i] == "#":
            counter = 0
            while counter <= ord(string[i + 1]):
                result += string[i + 2]
                counter += 1
            i += 2

        i += 1
    return result


stroka = 'Priveeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeet,I 111 wait you here toooooooooooooooooooooooooooooooooooo looooooooooooooooooooooooooooong'
print(stroka)
a = archive(stroka)
print(a)
b = unpack(a)
print(b)
