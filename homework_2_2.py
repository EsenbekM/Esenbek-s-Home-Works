#Заводим переменную "а" и аннулируем его
a=0         
for i in range (a, 20):  #Запускаем цикл FOR
    if i%2==0:   #Добавляем условие и проверяем на четность
        a+=2     #Если условия верны добавляем по 2
        print(a) #Выводим все четные числа в заданном диапазоне
