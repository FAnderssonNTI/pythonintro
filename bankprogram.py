balance = 100
menu = 0
rateVar = float(1.25)
rateConst = int(1)
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
        input("PRESS ENTER TO CONTINUE...")
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
        input("PRESS ENTER TO CONTINUE...")
    elif menu == 3:
        print(balance, "SEK")
        input("PRESS ENTER TO CONTINUE...")
    elif menu == 4:
        print("THE CURRENT RATE IS ", rateVar, "PER DAY")
        try:
            loan = int(input("HOW MUCH DO YOU WANT TO LOAN: "))
            try:
                days = int(input("HOW MANY DAYS DO YOU WANT TO LOAN FOR: "))
            except:
                print("ONLY NUMBERS ALLOWED")
        except:
            print("ONLY NUMBERS ALLOWED")
        for x in range(0, days):
            rateConst = rateConst * rateVar
        charge = rateConst * loan
        print("YOU WILL HAVE TO PAY", charge, "TO PAY OFF YOUR LOAN\n", "YOU HAVE", days, "DAYS TO PAY OFF YOUR LOAN")
        input("PRESS ENTER TO CONTINUE...")
    elif menu == 5:
        print("GOODBYE")
    else:
        print("NOT A VALID CHOICE")
