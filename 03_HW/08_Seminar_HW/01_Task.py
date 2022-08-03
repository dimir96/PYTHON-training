database = {}


def reading_file_to_dict(file):
    with open(f'{file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        data = [i.split(';') for i in data]
        database[file] = dict()

        line = dict()
        for i in data:
            for j in range(len(data[0])):
                line[data[0][j]] = i[j]
                database[file].append(line)
        print(database)
        # for i in data:
        #     database[file].append(tuple(i.split(';')))

reading_file_to_dict('parents')

# print(database)