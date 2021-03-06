elite_house=[
    {
        'flat': 1,
        'sold': True,
        'floor':1
    },
    {
        'flat': 2,
        'sold': False,
        'floor':1
    },
    {
        'flat': 3,
        'sold': False,
        'floor':1
    },
{
        'flat': 4,
        'sold': False,
        'floor':2
    },
    {
        'flat': 5,
        'sold': False,
        'floor':2
    },
    {
        'flat': 6,
        'sold': False,
        'floor':2
    },
{
        'flat': 7,
        'sold': False,
        'floor':3
    },
    {
        'flat': 8,
        'sold': False,
        'floor':3
    },
    {
        'flat': 9,
        'sold': False,
        'floor':3
    },
{
        'flat': 10,
        'sold': False,
        'floor':4
    },
    {
        'flat': 11,
        'sold': False,
        'floor':4
    },
    {
        'flat': 12,
        'sold': False,
        'floor':4
    },
{
        'flat': 13,
        'sold': False,
        'floor':5
    },
    {
        'flat': 14,
        'sold': False,
        'floor':5
    },
    {
        'flat': 15,
        'sold': True,
        'floor':5
    },
]
# Создал массив состоящий из словарей с данными дома и квартир
not_sold = []

# Написал функцию которая принимает ранее созданный массив, фильтрирует
def check_sold(elite_house):
    for free_flat in elite_house:
        if free_flat['sold'] == False:
            print('Flat number', free_flat['flat'], 'not sold')
            not_sold.append(free_flat)
check_sold(elite_house)

# Написал функцию которая принимает отфильтрованные данные, добавляет
# новое значение каждому из элементов отфильтрованных данных и возвращает
def buy_float(elite_house):
    for buy in elite_house:
        if buy['flat'] == 8:
            buy['sold'] = True
            print("You bought your flat", buy)
buy_float(elite_house)

# Напиcал функцию которая принимает массив ранее измененых данных,
# меняет значение в каждом из элементов и возращает измененные данные
def sale_house(elite_house):
    for sale in elite_house:
        if sale['sold'] == True:
            sale['sold'] = False
sale_house(elite_house)

# Написал функцию которая принимает массив ранее измененых данных,
# и поочередно выводит их в консоль
def show_changes(elite_house):
    for flat in elite_house:
        print(flat)
show_changes(elite_house)
