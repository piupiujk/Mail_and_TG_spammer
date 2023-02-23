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


def connect_email(email, app_password):
    """Подключение к почте и рассылка писем"""

    email = env.str('email')
    app_password = env.str('app_password')

    mail.connect_mail(email, app_password)

    mail.set_message('Тема сообщения', 'Сообщение')
    mail.send_message('Почта куда отпарвлять')


def id_base():
    """Получение id из csv файла в список"""

    tg_id_base = []

    with open('user_data.csv', encoding='utf-8') as base_file:
        base_reader = csv.reader(base_file, delimiter=',')
        for row in base_reader:
            tg_id_base.append(row[1])
        tg_id_base.pop(0)

    return tg_id_base


def connect_tg():
    """Подключение к тг и рассылка сообщений"""

    # https://my.telegram.org/apps - сайт где взять всю инфу об тг

    api_id = env.int('api_id')
    api_hash = env.str('api_hash')
    phone = env.str('phone')

    tg.connect_user(api_id=api_id, api_hash=api_hash, phone_number=phone)

    # user_id = tg.get_id_by_phone("Номер телефона")  # Что бы узнать id по номеру
    # tg.send_message(user_id=user_id, message='Введите сообщение')

    tg.set_message("**Крупное обновление в хомяке ☔.**\n\nОбновили дизайн, добавили множество новых и интересных товаров, таких как Баллы Мвидео, Заказы с Яндекс и Деливери за 50% от стоимости, Faceit, Лиры для всех, Турецкие Apple Gift карты и многое другое по самым лучшим ценам, большая часть товаров уже доступна к покупке, оставшиеся зальем совсем скоро, так же в течение недели появится Spotify, Discord Nitro, Спортмастер и многое другое, следите за обновлениями в боте.\n\nПриятных покупок💜")

    tg.set_image("C:/Users/Пользователь/Desktop/python/Projects/Mail_and_TG_spammer/Mail_and_TG_spammer/image_1.jpeg")

    # tg.start_selective_spam(id_base()) Должно работать, но пока рано запускать на всю базу



