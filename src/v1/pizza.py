crusts = {'thin', 'deepdish', 'hand_tossed'}
toppings = {'cheese', 'sausage', 'black_olive'}
meats = {'sausage'}

prices = {'thin': 8.0,
          'deepdish': 8.0,
          'hand_tossed': 8.0,
          'cheese': 1.0,
          'sausage': 1.5,
          'black_olive': 1.0}

def make_pizza(crust):
    if crust not in crusts:
        raise AttributeError('Invalid crust: ' + str(crust))
    return( {'crust': crust, 'toppings': []})

def get_crust(pizza):
    return(pizza['crust'])

def get_toppings(pizza):
    return(pizza['toppings'])

def add_topping(pizza, topping):
    if topping not in toppings:
        raise AttributeError('Invalid topping: ' + str(topping))
    get_toppings(pizza).append(topping)

def is_veggetarian(pizza):
    return(not (meats & set(get_toppings(pizza))))

def calculate_price(pizza):
    return -1

def remove_topping(pizza, topping):
    pass