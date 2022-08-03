def export_one_line(contacts):
    with open('export.txt', 'w') as file:
        for key in contacts:
            file.write(f'{key},{contacts[key]}\n')

def export_many_lines(contacts):
    with open('export.txt', 'w') as file:
        for key in contacts:
            file.write(f'{key}\n')
            for i in key:
                file.write(f'{i}\n')
            file.write('\n')