#Вывод информационного текста
print("Медалисты из Кыргызстана на Олимпийских играх в Токио 2020")
while True:    
  #Запускаем цикл WHILE с аргументом TRUE
    # Добавляем переменную medalists, внутри которой выводим инструкцию по правильному вводу
    # Также добавляем метод .upper() чтобы программа не зависила от ввода с маленькой или с большой буквы
    medalists=input("Для вывода медалистов напишите:" "\n" "Золото | Cеребро | Бронза " "\n" 
                    "Для выхода из программы:  Выйти""\n").upper()
    #Запускаем ветвление, которое проверяет наш ввод и выводит нужный текст
    if medalists=="ЗОЛОТО":
        print("Пока что у Кыргзстана нет золотой медали, но надеемся на лучшее)""\n")
    elif medalists=="СЕРЕБРО":
        print("1.Акжол Махмудов (Греко-Римская борьба)""\n""2.Айсулуу Тыныбекова (Вольная борьба)""\n")
    elif medalists=="БРОНЗА":
        print("1.Мээрим Жуманазарова (Вольная борьба)""\n")
    elif medalists=="ВЫЙТИ":
        print("АЛГА КЫРГЫЗСТАН!")
        break #Останавливаем программу если пользователь ввел "выйти"
    else: #Сообщаем о некорректности ввода пользователя
        print("Пожалуйста напишите корректно!""\n") #Не забываем об "\n" чтобы все выглядило красиво
