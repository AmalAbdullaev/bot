import telebot
import constants
import random
import os
from copy import deepcopy
import copy
bot = telebot.TeleBot(constants.token)

upd = bot.get_updates()

last_upd = upd[-1]



city = {
        "а": ["Архангельск" , "Алеппо", "Алушта",  "Алупка", "Амстердам",  "Абакан",  "Антверпен"],
        "б": [ "Бахчисараи", "Белгород",  "Белогорск", "Брянск",  "Барселона",  "Берлин",  "Берн"],
        "в": [ "Владивосток", "Волгоград",  "Вена",  "Венеция",  "Варшава",  "Винница",  "Воронеж"],
        "г": [ "Геленджик",  "Гамбург",  "Гагра",  "Гуково",  "Ганновер",  "Гданьск",  "Грозныи"],
        "д": [ "Дубаи ",  "Донецк",  "Донбасс",  "Данилов",  "Детройт",  "Дублин",  "Денвер"],
        "е": [ "Екатеринбург",  "Евпатория",  "Енисейск",  "Ейск",  "Егоров",  "Едрово",  "Евле"],
        "ж": [ "Женева",  "Железногорск",   "Жуков",  "Житомир",  "Жигулёвск",  "Жужуй",  "Железноводск"],
        "з": [ "Зеленоградск",  "Запорожье",  "Заволжье",  "Задар",  "Загреб",  "Зальцбург", "Звенигород"],
        "и": [ "Иерусалим",  "Ижевск",  "Иркутск",  "Инсар",  "Измаил",  "Иваново",  "Исламабад"],
        "к": [ "Киев",  "Кёльн",  "Кавасаки",  "Калининград",  "Кишинёв",  "Красноярск",  "Караганда"],
        "л": [ "Липецк",  "Луганск",  "Лас-Пальмас",  "Львов",  "Лейпциг",  "Лос-Анджелес",  "Лондон"],
        "м": [ "Магадан",  "Махачкала",  "Мичуринск",  "Москва",  "Мадрид",  "Малага",  "Мюнхен"],
        "н": [ "Нижний Новгород",  "Новокузнецк",  "Николаев",  "Новосибирск",  "Нагасаки",  "Нью-Йорк","Ницца"],
        "о": [ "Омск",  "Оренбург",  "Осло",  "Оттава",  "Омдурман",  "Оксфорд",  "Остенде"],
        "п": [ "Пенза",  "Пекин",  "Петропавловск-Камчатский",  "Подольск",  "Париж",  "Прага",  "Псков"],
        "р": [ "Ровно",  "Ростов на Дону",  "Рим",  "Росарио",  "Рио-де-Жанейро",  "Руан",  "Рига"],
        "с": [ "Саки",  "Санкт-Петербург",  "Сан-Франциско",  "Сан-Хосе",  "Сочи",  "Сиэтл",  "Стамбул"],
        "т": [ "Триполи",  "Томск",  "Тольятти",  "Токио",  "Таганрог",  "Торонто",  "Тель-Авив"],
        "у": [ "Уфа",  "Улан-Батор",  "Ужгород",  "Ульяновск",  "Урумчи",  "Уральск",  "Утрехт"],
        "ф": [ "Феодосия",  "Франкфурт",  "Фучжоу",  "Флоренция",  "Фокшани",  "Филадельфия","Фейсалабад"],
        "х": [ "Хабаровск",  "Херсон",  "Хиросима",  "Харьков",  "Хельсинки",  "Хьюстон","Ханты-Мансийск"],
        "ц": [ "Циндао",  "Цинциннати",  "Цицикар",  "Цюрих",  "Цивильск ",  "Цинциннати",  "Цимлянск"],
        "ч": [ "Чернигов",  "Чита",  "Чикаго",  "Черногорск",  "Челябинск",  "Чжэнчжоу",  "Честер"],
        "ш": [ "Шиен",  "Шарья",  "Шацк",  "Штутгарт",  "Шираз",  "Шуша",  "Шеффилд"],
        "щ": [ "Щёкино",  "Щёлково",  "Щербинка",  "Щецин",  "Щигры",  "ща",  "щу"],
        "э": [ "Эребру",  "Эрзурум",  "Эрмосильо",  "Эр-Рияд ",  "Эдинбург",  "Эльбасан",  "Эрдэнэт"],
        "ю": ["Южно-Сухокумск", "Южноуральск", "Юрга", "Юрмала",  "Юрга",  "Южно-Сахалинск", "Юджин"],
        "я": ["Якутск",  "Яхрома", "Ялгуба", "Ялта", "Янгон",  "Яунде", "Ярцево"]
        }




def have_word(letter,cities):
    try:
        return cities.get(letter).pop()
    except:
        return "!"


@bot.message_handler(content_types=['text'])
def handle_text(message):
    global true_letter
    global cities

    if (message.text == "/start"):
        bot.send_message(message.chat.id, "Я называю город, вы говорите на последнюю букву - и так далее. Мягкий знак и буква Ы ,"
                                          "не считаются. Только играй честно, если готов напиши - Давай играть")
    if(message.text == "Давай играть"):
        cities = copy.deepcopy(city)
        true_letter = "Л"
        bot.send_message(message.chat.id, "Давай начнем, Стамбул , тебе на Л")
    elif(message.text[0] == true_letter[0]):
        if message.text[len(message.text)-1] == "а":
            word = have_word("а", cities)
            if(word!="!"):
                bot.send_message(message.chat.id,word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word)-1].upper())
                true_letter = word[len(word)-1].upper()
                print(true_letter)
            else:bot.send_message(message.chat.id,"Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text)-1] == "б":
            word = have_word("б", cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "в":
            word = have_word("в",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "г":
            word = have_word("г",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "д":
            word = have_word("д",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "е":
            word = have_word("е",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "ж":
            word = have_word("ж",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "з":
            word = have_word("з",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "и":
            word = have_word("и",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "к":
            word = have_word("к",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "л":
            word = have_word("л",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "м":
            word = have_word("м",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "н":
            word = have_word("н",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "о":
            word = have_word("о",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "п":
            word = have_word("п",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "р":
            word = have_word("р",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "с":
            word = have_word("с",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "т":
            word = have_word("т",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "у":
            word = have_word("у",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "ф":
            word = have_word("ф",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "х":
            word = have_word("х",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "ц":
            word = have_word("ц",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "ч":
            word = have_word("ч",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "ш":
            word = have_word("ш",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "щ":
            word = have_word("щ",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "э":
            word = have_word("э",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "ю":
            word = have_word("ю",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        elif message.text[len(message.text) - 1] == "я":
            word = have_word("я",cities)
            if (word != "!"):
                bot.send_message(message.chat.id, word)
                bot.send_message(message.chat.id, "Тебе на букву " + word[len(word) - 1].upper())
                true_letter = word[len(word) - 1].upper()
            else:
                bot.send_message(message.chat.id, "Ты победил, я больше не знаю городов эту букву")
        else:
            bot.send_message(message.chat.id, "Давай другой город, у этого плохое окончание")
    else:
        bot.send_message(message.chat.id, "Нечестно играешь, давай нормально")
bot.polling(none_stop=True, interval=0)