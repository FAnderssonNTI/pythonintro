balance = 100
menu = 0
rate = float(1.25)
while menu != 5:
    print("***PRESS 1 TO DEPOSIT***\n" + "***PRESS 2 TO WITHDRAW***\n" + "***PRESS 3 TO SHOW YOUR ACCOUNT BALANCE***\n" + "***PRESS 4 TO TAKE A LOAN***\n" + "***PRESS 5 TO EXIT PROGRAM***")
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
        print("THE CURRENT RATE IS ", rate, "PER DAY")
        try:
            loan = int(input("HOW MUCH DO YOU WANT TO LOAN: "))
        except:
            print("ONLY NUMBERS ALLOWED")
        charge = loan * rate
        print("YOU WILL HAVE TO PAY ", charge, "TO PAY OFF YOUR LOAN")
    elif menu == 5:
        print("GOODBYE")
    else:
        print("NOT A VALID CHOICE")
