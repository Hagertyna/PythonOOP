class pComputer:
    def __init__(self):
        self.maxPrice = 45000
    def selling(self):
        print("selling price : {}".format(self.maxPrice))
    def setMaxPrice(self,price):
        self.maxPrice = price
pc = pComputer()
pc.selling()

#change the price
pc.maxPrice = 65000
pc.selling()

#lets use setter method
pc.setMaxPrice(70000)
pc.selling()