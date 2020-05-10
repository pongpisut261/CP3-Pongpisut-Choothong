class vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirconditioner(self):
        print("Turn on : Air")

class car(vehicle):
    def sayhi(self):
        print("Welcome to your Car")
class pickUp(vehicle):
    def sayhi(self):
        print("Welcome to your Pick up")
class van(vehicle):
    def sayhi(self):
        print("Welcome to your Van")
class estateCar(vehicle):
    def sayhi(self):
        print("Welcome to your Estate Car")

car1 = car()
car1.sayhi()
car1.turnOnAirconditioner()
pickUp1 = pickUp()
pickUp1.sayhi()
pickUp1.turnOnAirconditioner()
van1 = van()
van1.sayhi()
van1.turnOnAirconditioner()
estateCar1 = estateCar()
estateCar1.sayhi()
estateCar1.turnOnAirconditioner()