class BurgerMachine:
    def __init__(self):
        self.ingredients = {'bun': 10,
                            'beef patty': 5,
                            'chicken patty': 5,
                            'lettuce': 10,
                            'tomato': 10,
                            'cheese': 10}
        self.burgers_made = 0

    @staticmethod
    def make_burger(burger_type = null):
        if burger_type not in ('hamburger', 'cheese', 'burger'):
            print("Error: Invalid burger type.")

    if burger_type == 'hamburger':
        required_ingredients = {'bun': 1,
                                'beef patty': 1,
                                'lettuce': 2,
                                'tomato': 2}

    if burger_type == 'cheeseburger':
        required_ingredients = {'bun': 1,
                                'beef patty': 1,
                                'lettuce': 2,
                                'tomato': 2,
                                'cheese': 1}

    for ingredient, quantity in required_ingredients.items():
        if quantity > self.ingredients[ingredient]:
            print(f"Error: Not enough {ingredient}.")

    for ingredient, quantity in required_ingredients.items():
        self.ingredients[ingredient] -= quantity

    self.burgers_made += 1
    print(f"{burger_type.capitalize()} made!")

    def add_ingredients(self, ingredient, quantity):
        self.ingredients[ingredient] += quantity

    def restock(self):
        self.ingredients = {'bun': 10,
                            'beef patty': 5,
                            'chicken patty': 5,
                            'lettuce': 10,
                            'tomato': 10,
                            'cheese': 10}
