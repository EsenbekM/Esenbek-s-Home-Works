import random
#imported random library
num = random.randint(1, 100)
count = 0
#created counter variable
#and created variable for hints
vhot = num + 5
vhot_ = num - 5

hot = num + 10
hot_ = num - 10

near = num + 30
near_ = num - 30
#brouth out instructions
print(
    'Guess the number around 1-100: \n '
    'Print 0 for stop the game \n '
    '"very hot" - around 5 \n '
    '"hot" - around 10\n '
    '"cold" - around 30 \n '
    '"very cold - +30 or -30"'
)
#created variable for amount of attempts
tr = int(input("Print amount of attempts:  "))
print("Let's play! \nPrint your number: ")
#created variable for count remaining attempts
s=tr
#launched while cycle
while count != tr:
    #added condition for errors
    try:
        guess = int(input())
    except ValueError:
        print("Print only intiger numbers")
        continue
    # added condition for exit programm
    if guess == 0:
        print("Program is finish\nThanks for playing my game!\n\n\n <|Made by Esen4iik|>")
        break
    # added condition if player win
    if guess == num:
        count += 1
        print(f'You win from {count} time \nThanks for playing my game!\n\n\n <|Made by Esen4iik|>')
        break
    # added condition for hints
    elif guess <= vhot and guess >= vhot_:
        count += 1
        if guess < num:
            print("it's very hot, bigger")
        elif guess > num:
            print("it's very hot, lower")
    # added condition for hints
    elif guess <= hot and guess >= hot_:
        count += 1
        if guess < num:
            print("it's hot, bigger")
        elif guess > num:
            print("it's hot, lower")
    # added condition for hints
    elif guess <= near and guess >= near_:
        count += 1
        if guess < num:
            print("it's cold, bigger")
        elif guess > num:
            print("it's cold, lower")
    # added condition for hints
    elif guess < near and guess > 0 or guess > near_ and guess <= 100:
        count += 1
        if guess < num:
            print("it's very cold, bigger")
        elif guess > num:
            print("it's very cold, lower")
    # added condition if number bigger or lower then range
    else:
        print('Print namber into range')
    #print count remaining attempts
    s-=1
    print(f'You have {s} attempts')
# added condition if attempts ended
if count == tr:
    print(f'\nYour attempts is end\nThe target number was {num}\nThanks for playing my game!\n\n\n <|Made by Esen4iik|>')
