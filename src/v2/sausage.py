from src.v2.pizza import Pizza

class Sausage(Pizza):
    def __init__(self, pizza):
        self.base = pizza
    def is_veggetarian(self):
        return False
    def calculate_price(self):
        return (1.5 + self.base.calculate_price())
    def remove_topping(self, pizza_class):
        return self