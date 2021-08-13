data = ["O!", 705, "Megacom", 550, "Beeline", 770]
# Создаем пустые списки чтобы чтобы рассортировать список выше
names = []
code = []

# Добавил имена компаний в names и коды в code с помощью цикла
for g in data:
    if type(g)==str:
        names.append(g)
    elif type(g)==int:
        code.append(g)
print(names)    # ['O!', 'Megacom', 'Beeline'] - str
print(code)     # [705, 550, 770] - int

# Преобразовал списки names и code в кортеж с помощью метода tuple
names = tuple(names)
code = tuple(code)

# Создал словарь my_dict на основе кортежей names и code с помощью функции zip()
my_dict = dict(zip(names, code))
print(my_dict) # {'O!': 705, 'Megacom': 550, 'Beeline': 770}

# Обновил словарь с помощью метода update тем самым добавил к Ошке, Меге и Билайну дополнительные коды.
my_dict.update({"O!":[700, 705, 706, 707, 708, 709, 505, 500],
							   "Megacom":[551, 550, 555, 556, 557, 558, 559, 999],
							   "Beeline": [770, 775, 776, 777, 778, 779, 222]
							   })
							   
							   
print(my_dict)
 # вывод