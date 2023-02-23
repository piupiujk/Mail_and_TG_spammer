from social_spam import Mail, Telegram
from environs import Env
import csv

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


"""Получение id из csv файла в список"""

tg_id_base = []

with open('user_data.csv', encoding='utf-8') as base_file:
    base_reader = csv.reader(base_file, delimiter=',')
    for row in base_reader:
        tg_id_base.append(row[1])
    tg_id_base.pop(0)


"""Подключение к тг и рассылка сообщений"""


# https://my.telegram.org/apps - сайт где взять всю инфу об тг

api_id = env.int('api_id')
api_hash = env.str('api_hash')
phone = env.str('phone')


tg.connect_user(api_id=api_id, api_hash=api_hash, phone_number=phone)

user_id = tg.get_id_by_phone("Номер телефона")  # Что бы узнать id по номеру
tg.send_message(user_id=user_id, message='Введите сообщение')

