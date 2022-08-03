database = {}


def reading_file_to_dict(number_file):
    with open(f'{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))


def print_childrens(second_name):
    data = [i for i in database[1] if second_name in i]
    par_id = data[0][0]
    return [i for i in database[2] if i[1] == par_id]




reading_file_to_dict(1)
reading_file_to_dict(2)
print(database)


data = [i for i in database[1] if 'Ivanov' in i]
par_id = data[0][0]
children = [i for i in database[2] if i[1] == par_id]
print(data)
print(par_id)
print(children)