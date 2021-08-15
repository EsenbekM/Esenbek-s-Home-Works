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
        'sold': False,
        'floor':5
    },
]
#Создал списк из квартир

#создал пустой лист для корзины покупок
your_flat=[]


#Вывод квартир готовые к продаже
def check_sold(elite_house):
    print('Not sold Flats: ', end='')
    for free_flat in elite_house:
        if free_flat['sold'] == False:
            print('|',free_flat['flat'],'|',end='')

check_sold(elite_house)


#Покупка квартиры с изменением значения
def buy(elite_house):
    for g in elite_house:
        if g['flat']==i:
            g['sold']=True
            your_flat.append(g)
            print("You bought your flat", g['flat'],', in floor', g['floor'] ,'\n')

#Добавил в цикл для непрерывной покупки и для вывода ошибок
while True:
    i = int(input('\n''Write the number of the apartment you want to buy: ' '\n' 'If you want exit print 0' '\n'))
    if i>=1 and i<=15:
        buy(elite_house)
        check_sold(elite_house)

    elif i==0:
        break
    else:
        print('This flat not exist!')


#Вывод результата
def show_changes(elite_house):
    for flat in elite_house:
        print(flat)
show_changes(elite_house)

#Вывод корзины с покупками
print("Your flats:",your_flat)
