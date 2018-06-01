class BurgerSnob(object):
    def __init__(self, hunger_level, preference, eat_action, anger_action):
        self.hunger_level = hunger_level
        self.preference = preference
        self.eat_action = eat_action
        self.anger_action = anger_action

    #@property
    def get_hunger(self):
        return self.hunger_level

    #get_hunger.setter
    def set_hunger(self, level):
        self.hunger_level = level
        return None

    def fight_flight(self, burger):
        #present burger, get reaction
        self.burger = burger
        if burger.getCheeseType() == self.preference:
            self.eat_burger()
        else:
            self.attack()

    def eat_burger(self):
        #record stats
        #delete burger (stack/queue)
        #return glee
        print(self.eat_action)

    def attack(self, anger_action):
        print(self.anger_action)
