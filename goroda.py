file1 = open("file_city/а.txt")
file2 = open("file_city/б.txt")
file3 = open("file_city/в.txt")
file4 = open("file_city/г.txt")
file5 = open("file_city/д.txt")
file6 = open("file_city/е.txt")
file7 = open("file_city/ж.txt")
file8 = open("file_city/з.txt")
file9 = open("file_city/и.txt")
file10 = open("file_city/к.txt")
file11 = open("file_city/л.txt")
file12 = open("file_city/м.txt")
file13 = open("file_city/н.txt")
file14 = open("file_city/о.txt")
file15 = open("file_city/п.txt")
file16 = open("file_city/р.txt")
file17 = open("file_city/с.txt")
file18 = open("file_city/т.txt")
file19 = open("file_city/у.txt")
file20 = open("file_city/ф.txt")
file21 = open("file_city/х.txt")
file22 = open("file_city/ц.txt")
file23 = open("file_city/ч.txt")
file24 = open("file_city/э.txt")
file25 = open("file_city/ю.txt")
file26 = open("file_city/я.txt")


str1  = file1.read()
str2 = file2.read()
str3 =file3.read()
str4 =file4.read()
str5 = file5.read()
str6 =file6.read()
str7 =file7.read()
str8 =file8.read()
str9 =file9.read()
str10 = file10.read()
str11= file11.read()
str12 =file12.read()
str13= file13.read()
str14=file14.read()
str15=file15.read()
str16=file16.read()
str17=file17.read()
str18=file18.read()
str19=file19.read()
str20=file20.read()
str21=file21.read()
str22=file22.read()
str23=file23.read()
str24=file24.read()
str25=file25.read()
str26=file26.read()


arr1 = str1.split(' ')
arr2 = str2.split(' ')
arr3 = str3.split(' ')
arr4 = str4.split(' ')
arr5 = str5.split(' ')
arr6 = str6.split(' ')
arr7 = str7.split(' ')
arr8 = str8.split(' ')
arr9 = str9.split(' ')
arr10 = str10.split(' ')
arr11 = str11.split(' ')
arr12 = str12.split(' ')
arr13 = str13.split(' ')
arr14 = str14.split(' ')
arr15 = str15.split(' ')
arr16 = str16.split(' ')
arr17 = str17.split(' ')
arr18 = str18.split(' ')
arr19 = str19.split(' ')
arr20 = str20.split(' ')
arr21 = str21.split(' ')
arr22 = str22.split(' ')
arr23 = str23.split(' ')
arr24 = str24.split(' ')
arr25 = str25.split(' ')
arr26 = str26.split(' ')





city = {
        "а":  arr1,
        "б":   arr2,
        "в":   arr3,
        "г":    arr4,
        "д":    arr5,
        "е": arr6,
        "ж": arr7,
        "з": arr8,
        "и": arr9,
        "к": arr10,
        "л":   arr11,
        "м": arr12,
        "н": arr13,
        "о": arr14,
        "п": arr15,
        "р": arr16,
        "с": arr17,
        "т":arr18,
        "у": arr19,
        "ф": arr20,
        "х": arr21,
        "ц": arr22,
        "ч": arr23,
        "ш": ['Шадринск', 'Шали', 'Шарджа', 'Шарлеруа', 'Шартр', 'Шарыпово', 'Шарья',
              'Шатки', 'Шатура', 'Шахтёрск', 'Шахунья', 'Шацк', 'Шверин', 'Шебекино', 'Шевченко',
              'Шелехов', 'Шенкурск', 'Шеффилд', 'Шилка', 'Шимановск', 'Шклов', 'Шлиссельбург', 'Штутгарт',
              'Шумерля', 'Шумиха', 'Шуя', 'Шымкент', 'Шэньян'],

        "щ": [ "Щёкино",  "Щёлково",  "Щербинка",  "Щецин",  "Щигры",  "ща",  "щу"],
        "э": arr24,
        "ю": arr25,
        "я": arr26
        }