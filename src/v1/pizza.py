crusts = {'thin', 'deepdish', 'hand_tossed', 'stuffed'}
toppings = {'cheese', 'sausage', 'black_olive', 'pepperoni'}
dairy = {'cheese'}
meats = {'sausage', 'pepperoni'}

prices = {'thin': 8.0,
          'deepdish': 8.0,
          'stuffed': 8.0,
          'hand_tossed': 8.0,
          'cheese': 1.0,
          'pepperoni': 4.0,
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

def is_dairy_free(pizza):
    return(not (dairy & set(get_toppings(pizza))))
        


def calculate_price(pizza):
    base_price = prices[get_crust(pizza)]
    topping_cost = sum(prices[topping] for topping in get_toppings(pizza))
    return base_price + topping_cost
    #return 9.0 # EDITED FROM -1 TO 9.0

def remove_topping(toppings, topping):
    while topping in get_toppings(toppings):
        get_toppings(toppings).remove(topping)
    #topping for topping in toppings if not pizza
    #  == topping
    #[pizza for topping in toppings if not pizza == ]


    #if topping in get_toppings(pizza):
     #   get_toppings(pizza).remove(topping)
    #pass