call = 0


def count_calls():
    global call
    call += 1


def string_info():
    n = input('Введите слово: ', )
    count_calls()
    print(len(n), n.lower(), n.upper())


def is_contains(string, *list_to_search):
    string = string.upper()
    count_calls()
    for i in list_to_search:
        if string == i.upper():
            print(True)
            break
        elif i == list_to_search[-1] and string != i.upper():
            print(False)
        else:
            continue


string_info()
string_info()
string_info()
is_contains('Машина', 'Автомобиль', 'Авто', 'Тачка', 'Кар', 'Машина', 'Драндулет')
is_contains('Катя', 'Петя', 'Маша', 'Ира', 'Виталик', 'Катя')
is_contains('Россия', 'Китай', 'США', 'Турция')
print('Число использованных функций: ', call)
