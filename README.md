# Food Fight

### Feel the hunger


#### The Story So Far...

FoodFight is a program that models the human reaction to the pangs of hunger, with the unique preferences and reactions we all posess. 

Serve up meal types to various customers for financial reward, or face their wrath. Pit these hungry patrons against each other in the arena, and let their hunger levels determine who is victorious.

## Imports

```Python
import random
import string
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.style.use('bmh')
## Basic Burger Class
```Python
class BasicBurger():


    def __init__(self, patties=1, bun=True):
        self.patties = patties
        self.bun = bun
        self.food_type = "Basic Burger"
        self.topping = None
```
## Cheese Burger Class
```Python
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
```

## Generate A Brawler
```Python
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
        hunger = run.hungerGenerator()
        topping = run.toppingGenerator()
        eatAction = run.eatActionGenerator()
        angerAction = run.angerActionGenerator()
        favFood = run.favFoodGenerator()
        name = run.nameGenerator()
        wins = 0
        losses = 0
        atts = [hunger, topping, eatAction, angerAction, favFood, name, wins, losses]
        Brawler = Eater(*atts)
        return Brawler

```
## Generate Food
```Python
class FoodGenerator(object):


    def FoodTypeGenerator(self):
        run = BrawlerGenerator()
        food_type = run.favFoodGenerator()
        topping = run.toppingGenerator()
        food = [food_type, topping]
        return food

```
## Generate Customer
```Python
class Eater(object):
    def __init__(self, hunger_level, preference, eat_action, anger_action, fav_food, name, wins, losses):
        self.hunger_level = hunger_level
        self.fav_topping = preference
        self.eat_action = eat_action
        self.anger_action = anger_action
        self.fav_food = fav_food
        self.name = name
        self.wins = wins
        self.losses = losses


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


    def addWins(self):
        self.wins+=1
```
## The Battle Arena
```Python
class BattleArena():

    def matchUp(self, b1, b2):
        if b1.get_hunger() > b2.get_hunger():
            print("{} defeated {}!".format(b1.name, b2.name))
            b1.addWins()
        elif b1.get_hunger() == b2.get_hunger():
            print("Neither food warrior was vanquished")
        else:
            print("{} defeated {}!".format(b2.name, b1.name))
            b2.addWins()
```
## Reporting
```Python
class BattleReports():

    def CompareWins(self, eater1, eater2):
        data = {eater1.name:eater1.wins, eater2.name:eater2.wins}
        names = list(data.keys())
        values = list(data.values())
        fig, ax = plt.subplots()
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        plt.bar(range(len(data)), values, tick_label=names)
        plt.title('Total Wins')
        plt.xlabel('Challengers')
        plt.ylabel('Wins \n(Count)')
        plt.show()
 ```       
 ## Run It Example
 ```Python
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
```
