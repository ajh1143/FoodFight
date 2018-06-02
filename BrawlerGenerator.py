import random
class BrawlerGenerator(object):

    def hungerGenerator(self):
        hungerRand = random.randint(1,100)
        return hungerRand


    def toppingGenerator(self):
        burgerToppings = ['Cheddar', 'Jalapeno', 'Bacon', 'Pineapple']
        return random.choice(burgerToppings)


    def eatActionGenerator(self):
        actions = ['Gorge', 'Devour', 'Ingest']
        return random.choice(actions)


    def angerActionGenerator(self):
        angers = ['Throw', 'Slam', 'Rip', 'Smash']
        return random.choice(angers)


    def favFoodGenerator(self):
        favfood = ['Cheeseburger', 'Basic Burger', 'Taco']
        return random.choice(favfood)


    def nameGenerator(self):
        names = ['Terry', 'Eric', 'Jennifer', 'Ashley', 'Gerald']
        return random.choice(names)

    def generateBrawler(self):
        hunger = self.hungerGenerator()
        topping = self.toppingGenerator()
        eatAction = self.eatActionGenerator()
        angerAction = self.angerActionGenerator()
        favFood = self.favFoodGenerator()
        name = self.nameGenerator()
        atts = [hunger, topping, eatAction, angerAction, favFood, name]
        Brawler = Snob(*atts)
        return Brawler

