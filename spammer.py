from social_spam import Mail


mail = Mail()
mail.connect_mail('Почта с которой отправлять', 'Пароль Приложений')

mail.set_message('Message from docsap', 'How are you?')
mail.send_message('Почта куда отпарвлять')
