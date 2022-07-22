import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!$?`~,./\|;:%^*()_+=#"

while True:
    try:
        def passwordGenerator():
            passGen = int(input("What length of password do you want? "))
            manyPass = int(input("How many passwords would you like? "))
            if passGen <=0 or manyPass <=0:
                return "Password must be > 0!"
            else:
                print("--------------------------")
                for i in range(0, manyPass):
                    password = ""
                    for i in range(0, passGen):
                        randomPass = random.choice(chars)
                        password += randomPass
                    print(password)
                print("--------------------------")

        passwordGenerator()
        genAgain = input("Want to generate a new password? Y/N :")

        if genAgain == "Y" or genAgain =="Yes":
            passwordGenerator()
            break
        else:
            print("Thanks🍁")
            break

    except ValueError:
        print("Please enter a number!! ")




