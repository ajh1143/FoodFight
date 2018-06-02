import random
import string

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



class BrawlerGenerator(object):


    def hungerGenerator(self):
        hungerRand = random.randint(1,100)
        return hungerRand


    def toppingGenerator(self):
        burgerToppings = ['Cheddar', 'Jalapeno', 'Bacon', 'Pineapple']
        return random.choice(burgerToppings)


    def eatActionGenerator(self):
        actions = ['gorge', 'devour', 'ingest', 'swallow']
        return random.choice(actions)


    def angerActionGenerator(self):
        angers = ['throw', 'slam', 'rip', 'smash']
        return random.choice(angers)


    def favFoodGenerator(self):
        favfood = ['Cheeseburger', 'Basic Burger']
        return random.choice(favfood)


    def nameGenerator(self):
        first_name = random.choice(['Terry', 'Eric', 'Jennifer', 'Ashley', 'Gerald', "Matthew", "Aaron", "Paul",
                                                                                              "George", "Isaac"])
        last_names = random.choice(string.ascii_lowercase.upper())
        full_name = first_name+ " " + last_names + "."
        return full_name

    def generateBrawler(self):
        run = BrawlerGenerator()
        self.hunger = run.hungerGenerator()
        self.topping = run.toppingGenerator()
        self.eatAction = run.eatActionGenerator()
        self.angerAction = run.angerActionGenerator()
        self.favFood = run.favFoodGenerator()
        self.name = run.nameGenerator()
        atts = [self.hunger, self.topping, self.eatAction, self.angerAction, self.favFood, self.name]
        Brawler = Snob(*atts)
        return Brawler


class FoodGenerator(object):


    def FoodTypeGenerator(self):
        run = BrawlerGenerator()
        food_type = run.favFoodGenerator()
        topping = run.toppingGenerator()
        food = [food_type, topping]
        return food


class Snob(object):
    def __init__(self, hunger_level, preference, eat_action, anger_action, fav_food, name):
        self.hunger_level = hunger_level
        self.fav_topping = preference
        self.eat_action = eat_action
        self.anger_action = anger_action
        self.fav_food = fav_food
        self.name = name


    def get_hunger(self):
        return self.hunger_level


    def set_hunger(self, level):
        self.hunger_level = level


    def fight_flight(self, *food):
        # present burger, get reaction
        if food[0] is self.fav_food and food[1] is self.fav_topping:
            print("{} said: \"Yum! {} {}s are my favorite!\"".format(self.name, self.fav_topping, self.fav_food))
            self.eat(food[0], food[1])
        else:
            print("{} said: \"I only like {} {}s\"!".format(self.name, self.fav_topping, self.fav_food))
            self.attack(food[0], food[1])


    def eat(self, foodtype, topping):
        #record stats
        #delete burger (stack/queue?)
        #reduce hunger
        print("{} grabbed the {} {} and proceeded to {} it".format(self.name, topping, foodtype,  self.eat_action))
        self.set_hunger(int(self.get_hunger())-1)
        print("{}'s hunger level has decreased to {}!\n".format(self.name, self.get_hunger()))


    def attack(self, foodtype, topping):
        print("{} grabbed the {} {} and proceeded to violently {} it".format(self.name, topping, foodtype,
                                                                                       self.anger_action))

        self.set_hunger(int(self.get_hunger()) + 1)
        print("{}'s hunger level has risen to {}!\n".format(self.name, self.get_hunger()))

if __name__ == "__main__":

    Brawler = BrawlerGenerator()
    RandomBrawler1 = Brawler.generateBrawler()
    RandomBrawler2 = Brawler.generateBrawler()
    RandomBrawler3 = Brawler.generateBrawler()

    food = FoodGenerator()
    randFood = food.FoodTypeGenerator()

    RandomBrawler1.fight_flight(*randFood)
    RandomBrawler2.fight_flight(*randFood)
    RandomBrawler3.fight_flight(*randFood)


