#login
#showmenu
#menuselect
#vatcal
#pricecal
def logIn():
    userName = input("Username = ")
    password = int(input("Password :"))
    if userName == "admin" and password == 1234:
        return showMenu() , menuSelect()
    else:
        print("Not valid")
        return False
def showMenu():
    print("*" * 30)
    print("Welcome to IT Shop")
    print("Please select mode")
    print("1. price calculator")
    print("2. vat calculator")
    print("*" * 30)
def menuSelect():
    userSelected = int(input("Please select mode :"))
    if userSelected == 1:
        return priceCal()
    elif userSelected == 2:
        return vatCal()
def vatCal(totalprice):
    vat = 7/100
    result = totalprice +(totalprice * vat)
    print("Total amount (+vat 7%) =", result )
def priceCal():
    price1 = int(input("price1 ="))
    price2 = int(input("price2 ="))
    totalprice = price1 + price2
    print("totalprice =",totalprice)
    return vatCal(totalprice)
logIn()