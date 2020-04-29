userInput = input("Enter your username :")
passwordInput = int(input("Enter your passwod :"))
if userInput == "admin1" and passwordInput == 1234:
    print("-- Hello" , userInput ,"--")
    print("-- Welcome to Sawatdee Cafe --")
    print("*" * 40)
    print('Please selected manu')
    print("1.Espresso     50 THB")
    print("2.Americano    45 THB")
    print("3.Ice tea      55 THB")
    print("*" * 40)
    product = int(input("Selectd manu : "))
    number = int(input("How many do you want :"))
    if product > 3 :
        print("Not valid")
    elif product == 1 :
        print("*" * 40)
        print("price = ", 50 * number , "THB")
    elif product == 2 :
        print("*" * 40)
        print("price = ", 45 * number , "THB")
    else:
        print("*" * 40)
        print("price = ", 55 * number , "THB")
    print("*" * 40)
    print("** Thank you **")

else: print("Please try again")



