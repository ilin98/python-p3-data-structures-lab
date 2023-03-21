spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [dish.get("name") for dish in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [dish for dish in spicy_foods if dish["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for dish in spicy_foods:
        print(f"{dish['name']} ({dish['cuisine']}) | Heat Level: {'🌶' * dish['heat_level']}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    new_cuisine = ([dish for dish in spicy_foods if dish["cuisine"] == cuisine])
    return new_cuisine[0]

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    heat_level = [dish.get("heat_level") for dish in spicy_foods]
    sum = 0
    for heat in heat_level:
        sum += heat
    return sum / len(heat_level)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

create_spicy_food(spicy_foods, {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10})
