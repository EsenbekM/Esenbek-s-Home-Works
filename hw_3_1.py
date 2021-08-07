
#Пример типа данных лист для добавления в словарь
list_exemple=["str",123,2.3]

#Пример типа данных словарь для добавления в словарь
dictionary_example={
    "name":"Esenbek",
    "age": 18
}

#Пример типа данных буул для добавления в словарь
x=True

#Создаю словарь который содержит в себе все типы данных которые я знаю
dictionary ={
    "str":"string",
    "int":12345,
    "float":2.32,
    "list":list_exemple,
    "range":range(6),
    "dictionary":dictionary_example,
    "bool":x
}

#Вывожу все ключи и значения в отдельные строки через for, чтобы было красиво)
for key, value in dictionary.items():
    print(key, value)
