#Bill
#food menu
#price
#total price

menuList = []
priceList = []
def receipt():
    print("--- Sawatdee Cafe ---")
    for menu in range(len(menuList)):
        print(menuList[menu] , "=" , priceList[menu] , "Baht")
    sum = 0
    for price in priceList:
        sum += int(price)
    print("*" * 30)
    print("Total price =" , sum)
    print("*" * 30)
    print(" --- Thank you ---")

while True:
    foodName = input("Please enter food :")
    if foodName.lower() == "exit":
        break
    else:
        foodPrice = input("Please enter price :")
        menuList.append(foodName)
        priceList.append(foodPrice)

receipt()