from hw_8_lists import *
import colorama
from colorama import Fore, Back, Style
colorama.init()


# creat function for choose one list
def choose_list():
    while 1:
        l = input(Fore.BLACK + Back.BLUE + "CONTACTS: |classmates / family / taxi / food / SOS|\nChoose contacts for editing: ").lower()
        if l == 'classmates':
            list.append(classmates)
            break
        elif l == 'family':
            password = (10-2+10-9+2-3-2)**(43-34-19+2+16-3)
            if int(input("Enter password: ")) == password:
                list.append(family)
                break
            else:
                print("Access denied!")
                continue
        elif l == 'sos':
            list.append(SOS)
            break
        elif l == 'food':
            list.append(food)
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
    for contact in list[0]:
        if contact['name'] == lst or contact['phone'] ==  lst:
            return contact

# creat function for add
def add_contact(lst):
    name = input("Creat new contact\nEnter name: ").title()
    phone = input("Enter phone: ")
    if find_contact(name) or find_contact(phone):
        print('Contact already exist!')
        q = input('Do you want add second number?  y/n: ')
        if q == 'y':
            for i in lst:
                if i['name'] == name:
                    phone = input("Enter second phone: ")
                    i.update((dict(second_phone=phone)))
    else:
        contact = dict(pozition=((list[0][::-1][0]["pozition"]) + 1), name=name.title(), phone=phone)
        lst.append(contact)
        return contact

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
            if find_contact(n) or find_contact(phone):
                print('Contact already exist!')
            else:
                i["name"] = n
                i["phone"] = phone

# creat main function for all program
def main():
    while 1:
        show_all_contacts(list[0])
        command = input("Enter comand for interaction ' 1 - edit / 2 - delete / 3 - add'. ' 0 - q' for quite: ").lower()
        if command == 'edit' or command == '1':
            edit_contact(list[0])
        elif command == 'delete'or command == '2':
            delete_contact(list[0])
        elif command == 'add' or command == '3':
            add_contact(list[0])
        elif command == 'q' or command == '0':
            print("Program is finish")
            break
        else:
            print('Incorrect command!')
