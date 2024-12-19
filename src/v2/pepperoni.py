from src.v2.pizza import Pizza

class Pepperoni(Pizza):
    def __init__(self, pizza):
        self.base = pizza
    def is_veggetarian(self):
        return False
    def calculate_price(self):
        return ( + self.base.calculate_price())
    def remove_topping(self, pizza):
        if isinstance(self, pizza):
            return self.base
        return self
    def is_dairy_free(self):
        return True