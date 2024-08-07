import telebot

bot = telebot.TeleBot('7479167015:AAG9uxLv0iUY28lAa_q1Bgrf7XlUvGQt41Q')


@bot.message_handler(commands=['start'])
def command1(massage):
    bot.send_message(massage.chat.id, '**Вас привествует участник марафона**',
                     parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def command2(massage):
    bot.send_message(massage.chat.id, text= '[_Основы языка python_](https://pythontutor.ru/)',parse_mode = 'Markdown')


@bot.message_handler(commands=['feedback'])
def command3(massage):
    bot.send_message(massage.chat.id, 'Жду результаты дз',
                     parse_mode='Markdown')


bot.infinity_polling()
