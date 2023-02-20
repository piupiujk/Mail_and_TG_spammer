from social_spam import Mail, Telegram
from environs import Env

env = Env()
env.read_env()

mail = Mail()
tg = Telegram()


"""!!!!!!!!!!!!!!!!!!
Сделать все в функиях
!!!!!!!!!!!!!!!!!!"""


"""Подключение к почте и рассылка писем"""


email = env.str('email')
app_password = env.str('app_password')


mail.connect_mail(email, app_password)

mail.set_message('Тема сообщения', 'Сообщение')
mail.send_message('Почта куда отпарвлять')


"""Получение почт из txt файла в список"""

email_base = []

with open('base_email.txt', 'r') as base_txt:
    for line in base_txt:
        email_base.append(line.strip())


"""Подключение к тг и рассылка сообщений"""


# https://my.telegram.org/apps - сайт где взять всю инфу об тг

api_id = env.int('api_id')
api_hash = env.str('api_hash')
phone = env.str('phone')


tg.connect_user(api_id=api_id, api_hash=api_hash, phone_number=phone)

user_id = tg.get_id_by_phone("Номер телефона")  # Что бы узнать id по номеру
tg.send_message(user_id=user_id, message='Введите сообщение')

