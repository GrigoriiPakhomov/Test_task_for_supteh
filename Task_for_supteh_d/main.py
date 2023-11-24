import telebot
from datetime import datetime

TOKEN = '6649882241:AAETG76t9Yxm2JS_bWsKBsqqLq0r5_bxpCg'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Могу назвать вам текущее число и день недели.')

@bot.message_handler(commands=['Какой сегодня день?'])
def get_current_date(message):
    now = datetime.now()
    current_date = now.strftime('%d.%m.%Y')
    day_of_week = now.strftime('%A')

    response = f'Сегодня {current_date}, {day_of_week}.'
    bot.send_message(message.chat.id, response)

bot.polling()