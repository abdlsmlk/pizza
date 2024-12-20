from src.v2.pizza import Pizza

class BlackOlive(Pizza):
    def __init__(self, pizza):
        self.base = pizza
    def is_veggetarian(self):
        return True
    def calculate_price(self):
        return (1 + self.base.calculate_price())
    def remove_topping(self, pizza_class):
        return self