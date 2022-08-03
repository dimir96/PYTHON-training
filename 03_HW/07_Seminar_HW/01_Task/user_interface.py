import menu
import generator
import exporter
import logger

def program_start():

    contacts = dict()
    while True:
        print('MAIN MENU')
        menu_command = menu.user_menu()
        if menu_command == 'g':
            count = int(input('Введите количество контактов: '))
            contacts = generator.contact_generator(count)
            logger.line_logger('g', count)
        if menu_command == '1':
            exporter.export_one_line(contacts)
            logger.line_logger('s', count)
        if menu_command == '2':
            exporter.export_many_lines(contacts)
            logger.line_logger('s', count)
