def user_menu():
    while True:
        print('g - для генерации контактов; s - для экпорта контактов')
        menu = input('Введите команду:')
        if menu == 's':
            print('Выберите формат экспотра: 1 для экспотра контакта в одну строку; 2 - для экспорта каждого элемента с новой строки')
            menu = input('Введите команду:')
            return menu
        if menu == 'g':
            return menu
        else:
            continue