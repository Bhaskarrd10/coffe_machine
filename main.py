MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1. print report of all coffee machine resources.

def is_resource_sufficient(order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("There is no enough water")
            return False
        return True
def process_coins():
    print("Please insert coins")
    total = int(input("how many quareters?")) * 0.25
    total = int(input("how many dimes?")) * 0.25
    total = int(input("how many nickles?")) * 0.25
    total = int(input("how many pennies?")) * 0.25

is_on = True,
while is_on:
    choice = input("what would you like? (expresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
