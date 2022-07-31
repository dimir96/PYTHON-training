from datetime import datetime as dt

def calc_logger(data):
    value, result = data
    time = dt.now()
    with open('log.csv', 'a') as file:
        file.write(f'{time}; {value} = {result}\n')