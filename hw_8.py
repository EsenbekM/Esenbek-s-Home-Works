#created lists
classmates = [
    {
        "pozition": 1,
        "name": "Bekbolsun",
        "phone": "(0507)20-04-27"
    },
    {
        "pozition": 2,
        "name": "Islam",
        "phone": "(0770)20-06-18"
    },
    {
        "pozition": 3,
        "name": "Adahan",
        "phone": '(0707)77-09-99'
    },
    {
        "pozition": 4,
        "name": "Batyr",
        "phone": "(0702)31-43-85"
    },
    {
        "pozition": 5,
        "name": "Esenbek",
        "phone": "(0708)60-16-01"
    },
    {
        "pozition": 6,
        "name": "Emirlan",
        "phone": "(0999)17-18-77"
    },
]

family = [
    {
        "pozition": 1,
        "name": "Father",
        "phone": "(0554)25-07-64"
    },
    {
        "pozition": 2,
        "name": "Mother",
        "phone": "(0500)40-15-59"
    },
    {
        "pozition": 3,
        "name": "Old_brother",
        "phone": '(0703)49-11-91'
    },
    {
        "pozition": 4,
        "name": "Yong_brother",
        "phone": "(0500)82-55-25"
    },
    {
        "pozition": 5,
        "name": "Sister",
        "phone": "(0705)99-91-94"
    },
]

SOS = [
    {
        "pozition": 1,
        "name": "Fire_service",
        "phone": "101 "
    },
    {
        "pozition": 2,
        "name": "Police",
        "phone": "102"
    },
    {
        "pozition": 3,
        "name": "Ambulance",
        "phone": '103'
    },
    {
        "pozition": 4,
        "name": "Mes",
        "phone": "104"
    },
]

taxi = [
    {
        "pozition": 1,
        "name": "Tumar_taxi",
        "phone": "(0706)00-19-39"
    },
    {
        "pozition": 2,
        "name": "Jorgo",
        "phone": "(0705)77-20-22"
    },
    {
        "pozition": 3,
        "name": "Lovi",
        "phone": '(0552)14-22-00'
    },
    {
        "pozition": 4,
        "name": "Record_taxi",
        "phone": "(0705)00-12-34"
    },
    {
        "pozition": 5,
        "name": "Alpha",
        "phone": "(0550)65-77-77"
    },
    {
        "pozition": 6,
        "name": "Bars",
        "phone": "(0559)61-70-80"
    },
]

food = [
    {
        "pozition": 1,
        "name": "Empire_pizza",
        "phone": "(0312)62-25-02"
    },
    {
        "pozition": 2,
        "name": "Do-do_pizza",
        "phone": "(0312)55-05-50"
    },
    {
        "pozition": 3,
        "name": "Kfc",
        "phone": '(0550)88-02-29'
    },
    {
        "pozition": 4,
        "name": "Domino",
        "phone": "(0312)90-09-00"
    },
    {
        "pozition": 5,
        "name": "Daamdu",
        "phone": "(0500)49-90-94"
    },
]

#creat list for append
list = []

# creat function for choose one list
def choose_list():
    while 1:
        l = input("CONTACTS: |classmates / famaly / taxi / food / SOS|\nChoose contacts for editing: ").lower()
        if l == 'classmates':
            list.append(classmates)
            break
        elif l == 'family':
            password = "1234"
            if input("Enter password: ") == password:
                list.append(family)
                break
            else:
                print("Access denied!")
        elif l == 'sos':
            list.append(SOS)
            break
        elif l == 'taxi':
            list.append(taxi)
            break
        else:
            print("Incorrect command!")

        return list

# creat function for  show
def show_all_contacts(lst):
    for i in lst:
        print(*i.values())

# creat function for find
def find_contact(lst):
    a = input("Enter 'n' - if you want find from name\nEnter 'p' - if you want find from phone")
    if a == "n":
        name = input("Enter name: ").title()
        for i in lst:
            if i["name"] == name:
                print(f"It's found in {i['pozition']} pozition\nName: {i['name']}\nPhone: {i['phone']}")
    elif a == "p":
        phone = input("Enter phone: ")
        for i in lst:
            if i["phone"] == phone:
                print(f"It's found in {i['pozition']} pozition\nName: {i['name']}\nPhone: {i['phone']}")
    else:
        print("Incorrect command!")

# creat function for add
def add_contact(lst):
    name = input("Creat new contact\nEnter name: ")
    phone = input("Enter phone: ")
    contact = dict(pozition=((list[0][::-1][0]["pozition"]) + 1), name=name.title(), phone=phone)
    lst.append(contact)

# creat function for delete
def delete_contact(lst):
    name = input("Enter name: ").title()
    for i in lst:
        if i["name"] == name:
            lst.remove(i)

# creat function for edit
def edit_contact(lst):
    name = input("Enter name: ").title()
    for i in lst:
        if i["name"] == name:
            n = input("Enter new name: ")
            phone = input("Enter new phone: ")
            i["name"] = n
            i["phone"] = phone

# creat main function for all program
def main():
    while 1:
        show_all_contacts(list[0])
        command = input("Enter comand for interaction 'find / edit / delete / add'. 'q' for quite: ").lower()
        if command == 'find':
            find_contact(list[0])
        elif command == 'edit':
            edit_contact(list[0])
        elif command == 'delete':
            delete_contact(list[0])
        elif command == 'add':
            add_contact(list[0])
        elif command == 'q':
            print("Program is finish")
            break
        if command == 'b':
            choose_list()

#run function and add error exeption
try:
    choose_list()
    main()
except IndexError:
    print()
    
