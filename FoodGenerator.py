class FoodGenerator(object):

    def FoodTypeGenerator(self):
        run = BrawlerGenerator()
        food_type = run.favFoodGenerator()
        topping = run.toppingGenerator()
        food = [food_type, topping]
        return food
