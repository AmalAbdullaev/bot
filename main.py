import telebot
import constants
import goroda
import copy

bot = telebot.TeleBot(constants.token)
upd = bot.get_updates()
last_upd = upd[-1]
cities = copy.deepcopy(goroda.city)
results = []
letter = "!"

@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        global cities, letter
        client_city = message.text

        if(message.text == "/start"):
            bot.send_message(message.chat.id, "Отправь мне город, города на Ь,Й,Ы,Ъ не считаются ")
            results.clear()
            letter = "!"
        elif((letter==client_city[0] or letter== "!") and client_city in cities.get(client_city[0].lower()) and client_city not in results ):
            my_city = cities.get(client_city[len(client_city)-1].lower()).pop()
            if(my_city[0]!=client_city[len(client_city)-1]):
                my_city = cities.get(client_city[len(client_city) - 1].lower()).pop()
            letter = my_city[len(my_city) - 1].upper()
            if(letter=="ь" or letter == "ы" or letter=="ъ" or letter=="й"):
                letter = my_city[len(my_city) - 2].upper()
            bot.send_message(message.chat.id, my_city)
            results.append(message.text)
            results.append(my_city)

        else:
            bot.send_message(message.chat.id,"Ты продул, давай сначала, пиши /start и начнем")
            results.clear()
            letter = "!"

    except(IndexError):
        bot.send_message(message.chat.id, "Я проиграл, больше не знаю городов на эту букву, давай еще, пиши /start и начнем")
        cities = copy.deepcopy(goroda.city)


bot.polling(none_stop=True, interval=0)
