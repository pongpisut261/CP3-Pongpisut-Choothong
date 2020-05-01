#login
#showmenu
#menuselect
#vatcal
#pricecal
def logIn():
    userName = input("Username = ")
    password = int(input("Password :"))
    if userName == "admin" and password == 1234:
        return True
    else:
        print("Not valid")
        return False
def showMenu():
    print("*" * 30)
    print("Welcome to IT Shop")
    print("Please select mode")
    print("1. vat calculator")
    print("2. price calculator")
    print("*" * 30)
def selectMode():
    userSelected = int(input("Please select mode :"))
    return userSelected
def vatCal(totalprice):
    vat = 7/100
    return totalprice + (totalprice * vat)
def priceCal():
    price1 = int(input("price1 ="))
    price2 = int(input("price2 ="))
    return vatCal(price1 + price2)

if logIn() == True:
    showMenu()
    mode = selectMode()
    if mode == 1:
        totalprice = int(input("totalprice ="))
        print("total amount =" ,vatCal(totalprice))
    elif mode == 2:
        print("total amount =" ,priceCal())