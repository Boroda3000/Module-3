def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if recipient == sender:
        return print('Нельзя отправить письмо самому себе!')
    respond_1 = ['Невозможно отправить письмо с адреса', sender, 'на адрес', recipient]
    respond_2 = ['Письмо успешно отправлено с адреса', sender, 'на адрес', recipient]
    respond_3 = ['НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient]
    if '@' in recipient:
        if sender == 'university.help@gmail.com':
            return print(respond_2)
        else:
            return print(respond_3)
    else:
        return print(respond_1)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')