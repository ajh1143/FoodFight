class BasicBurger():


    def __init__(self, patties=1, bun=True):
        self.patties = patties
        self.bun = bun
        self.food_type = "Basic Burger"
        self.topping = None


class Cheeseburger(BasicBurger):


    def __init__(self, cheesetype ="Cheddar", cheesecount=1, patties = 1):
        self.cheesetype = cheesetype
        self.cheesecount = cheesecount
        self.patties =patties
        self.food_type = "Cheeseburger"
        self.topping = None


    def setMeatPatties(self, newPatties):
        self.patties = newPatties


    def getMeatPatties(self):
       # print("This cheeseburger has {} Meat Patties".format(self.patties))
        return self.patties


    def setCheeseType(self, type):
        self.cheesetype = type


    def getCheeseType(self):
       # print("This cheeseburger has {} cheese".format(self.cheesetype))
        return self.cheesetype


    def setCheeseSlices(self, slices):
        self.cheesecount = slices
        return self.cheesecount


    def getCheeseSlices(self):
        return self.patties
