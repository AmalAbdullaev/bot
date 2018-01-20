import telebot
import constants

bot = telebot.TeleBot(constants.token)
upd = bot.get_updates()
last_upd = upd[-1]
file = open("city.txt",'r', encoding='utf-8',)
cities = ""


send = ["!"]
all_cities = []

def out(send,message):
    el = send.pop()
    if(el == "!" or el[len(el)-1].upper()==message.text[0]):
        return True
    elif(el=="!" or el[len(el)-1].upper()=="Ь" or el[len(el)-1].upper()=="Ъ" or el[len(el)-1].upper()=="Ы" ):
        if(el[len(el)-2].upper()==message.text[0]):
            return True
        else:
            return False
    else:
        return False


@bot.message_handler(content_types=['text'])
def handle_text(message):
    global start
    global cities
    global file
    try:
        if (message.text == "/start"):
            bot.send_message(message.chat.id, "Поехали, посмотрим на что ты способен  ")
            send.clear()
            send.append("!")
            file = open("city.txt",'r', errors='ignore',encoding='utf-8')
            cities = file.read()
            all_cities.clear()
        elif(cities.find(message.text)!=-1 and out(send,message) and message.text not in all_cities):
            cities = cities.replace(message.text, '')
            start = cities.find(message.text[len(message.text)-1].upper()) #ищем город на последнюю букву города которую назвал клиент
            if (start == -1):
                start = cities.find(message.text[len(message.text) - 2].upper())
            end  =  cities.find("\n",start)
            answer_city =  cities[start:end]
            bot.send_message(message.chat.id, answer_city)
            send.append(answer_city)
            all_cities.append(answer_city)
            all_cities.append(message.text)
            cities = cities.replace(answer_city,'')
        elif(message.text[0] == "."):
            city = message.text[1:]
            file.write("\n" + city)
            bot.send_message(message.chat.id, "Запомнил")

        else:
            bot.send_message(message.chat.id, "Тебе со мной не тягаться, ты проиграл")
    except(IndexError):
        bot.send_message("Я проиграл")


bot.polling(none_stop=True, interval=0)
