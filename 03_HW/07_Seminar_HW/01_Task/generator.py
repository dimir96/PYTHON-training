from random import randint
def gen_name():
    data_list = ['Ваня', 'Саша', 'Петя', 'Вася']
    return data_list[randint(0,len(data_list)-1)]

def gen_surname():
    data_list = ['Иванов', "Петров", "Сидоров", "Рибентроп"]
    return data_list[randint(0,len(data_list)-1)]

def gen_phone():
    data_list = ['+48 283 484 382', "+48 323 543 593", "+48 237 543 345", "+48 234 542 656"]
    return data_list[randint(0,len(data_list)-1)]

def gen_birth_date():
    data_list = ['19.03.1958', "23.12.1996", "30.04.1987", "30.08.1970"]
    return data_list[randint(0,len(data_list)-1)]


def contact_generator(count=10):
    i = 1
    contact_dict = dict()
    while i < count:
        contact_dict[i] = [gen_name(),gen_surname(),gen_phone(),gen_birth_date()]
        i += 1
    print(contact_dict)
    return contact_dict