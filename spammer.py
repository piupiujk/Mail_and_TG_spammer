from social_spam import Mail, Telegram

mail = Mail()
tg = Telegram()


"""Подключение к почте и рассылка писем"""


email = 'Почта'
app_password = 'Пароль приложения'

mail.connect_mail(email, app_password)

mail.set_message('Тема сообщения', 'Сообщение')
mail.send_message('Почта куда отпарвлять')


"""Подключение к тг и рассылка сообщений"""


# https://my.telegram.org/apps - сайт где взять всю инфу об тг

api_id = ''
api_hash = ''
phone = ''

tg.connect_user(api_id=api_id, api_hash=api_hash, phone_number=phone)

user_id = tg.get_id_by_phone("Номер телефона")  # Что бы узнать id по номеру
tg.send_message(user_id=user_id, message='Введите сообщение')

