from time import time

def line_logger(proces, count=0):
    with open('log.txt', 'a') as file:
        if proces == 'g':
            file.write(f'{time()}\timport\t{count}contacts\n')
        if proces == 's':
            file.write(f'{time()}\texport\t{count}contacts\n')