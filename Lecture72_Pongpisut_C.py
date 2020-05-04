menuList = []
def receipt():
    print("--- Sawatdee Cafe ---")
    sum = 0
    for menu in range(len(menuList)):
        print(menuList[menu][0] ,"=" , menuList[menu][1],"THB")
        sum += int(menuList[menu][1])
    print("Total price =", sum , "THB")
while True:
    foodName = input("Please enter food :")
    if foodName.lower() == "exit":
        break
    else:
        foodPrice = input("Please enter price :")
        menuList.append([foodName , foodPrice])

receipt()
