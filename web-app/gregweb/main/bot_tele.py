import telebot

bot = telebot.TeleBot('6884775017:AAHoStRR5iTROu0h-V984WMYVVTA3_bUkBw')

@bot.message_handler(commands=['start'])
def main_telegram(message):
    bot.send_message(message.chat.id, 'Поздравляем, теперь вы можете получать заказы!')
    print(message.chat.id)


bot.polling(none_stop=True)
