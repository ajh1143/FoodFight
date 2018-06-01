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


    def fight_flight(self, food):
        # present burger, get reaction
        if food.food_type == self.fav_food and self.fav_topping == food.getCheeseType():
            print("Yum! {} {}s are my favorite!".format(self.fav_topping, self.fav_food))
            self.eat(food.food_type)
        else:
            print("I only like {} {}s!".format(self.fav_topping, self.fav_food))
            self.attack(food.food_type)


    def eat(self, food):
        #record stats
        #delete burger (stack/queue?)
        #reduce hunger
        print("{} grabbed the {} and proceeded to {}".format(self.name, food, self.eat_action))
        self.set_hunger(int(self.get_hunger())-1)
        print("{}'s hunger level has decreased to {}!".format(self.name, self.get_hunger()))


    def attack(self, food):
        print("{} grabbed the {} and proceeded to violently {} it".format(self.name, food, self.anger_action))
        self.set_hunger(int(self.get_hunger()) + 1)
        print("{}'s hunger level has risen to {}!".format(self.name, self.get_hunger()))
