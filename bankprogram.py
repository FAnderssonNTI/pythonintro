balance = 100
menu = 0
while menu != 4:
    print("***PRESS 1 TO DEPOSIT***\n" + "***PRESS 2 TO WITHDRAW***\n" + "***PRESS 3 TO SHOW YOUR ACCOUNT BALANCE***\n" + "***PRESS 4 TO EXIT PROGRAM***")
    try:
        menu = int(input("MAKE YOUR SELECTION: "))
    except:
        print("ONLY NUMBERS ALLOWED!")
    if menu == 1:
        print("YOU HAVE ", balance, "SEK IN YOUR ACCOUNT")
        try:
           balance = balance + int(input("HOW MUCH DO YOU WISH TO INSERT: "))
        except:
            print("ONLY NUMBERS ALLOWED")
    elif menu == 2:
        print("YOU HAVE ", balance, " SEK IN YOUR ACCOUNT")
        try:
            withdraw = int(input("HOW MUCH DO YOU WISH TO WITHDRAW: "))
        except:
            print("ONLY NUMBERS ALLOWED!")
        if (balance - withdraw) >= 0:
            balance = balance - withdraw
            print("YOU NOW HAVE ", balance, " SEK IN YOUR ACCOUNT")
        else:
            print("YOU CAN'T WITHDRAW THAT AMOUNT")
    elif menu == 3:
        print(balance, "SEK")
    elif menu == 4:
        print("GOODBYE")
    else:
        print("NOT A VALID CHOICE")
#qweasd