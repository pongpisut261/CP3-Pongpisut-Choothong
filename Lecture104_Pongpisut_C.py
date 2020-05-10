class customer:
    name = ""
    lastname = ""
    age = 0
    def addCart(self):
        print("add product to",self.name,self.lastname,"'s cart")

customer1 = customer()
customer1.name = "Pongpisut"
customer1.lastname = "Choothong"
customer1.addCart()

customer2 = customer()
customer2.name = "David"
customer2.lastname = "Beckham"
customer2.addCart()

customer3 = customer()
customer3.name = "Michael"
customer3.lastname = "Owen"
customer3.addCart()

customer4 = customer()
customer4.name = "Sonram"
customer4.lastname = "Teppitak"
customer4.addCart()
