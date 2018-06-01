class Snob(object):
    def __init__(self, hunger_level, preference, eat_action, anger_action, fav_food):
        self.hunger_level = hunger_level
        self.fav_topping = preference
        self.eat_action = eat_action
        self.anger_action = anger_action
        self.fav_food = fav_food


    def get_hunger(self):
        return self.hunger_level


    def set_hunger(self, level):
        self.hunger_level = level
        return None


    def fight_flight(self, food):
        # present burger, get reaction
        if food.food_type == self.fav_food and self.fav_topping == food.getCheeseType():
            print("Yum! {} {}'s are my favorite!".format(self.fav_topping, self.fav_food))
            self.eat_burger()
        else:
            print("I only like {} {}!".format(self.fav_topping, self.fav_food))
            self.attack()


    def eat_burger(self):
        #record stats
        #delete burger (stack/queue?)
        #reduce hunger
        print(self.eat_action)
        self.set_hunger(self.get_hunger()-1)


    def attack(self):
        print(self.anger_action)
