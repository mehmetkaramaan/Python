MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

water = 300
milk = 200
coffee = 100
money = 0

def insertCoins():
    global quarters,dimes,nickles,pennies,total
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_ = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    total = round(total_)
def coffeeMachine():
    global MENU,water,milk,coffee,money
    choice = input("What would you like? (espresso/latte/cappuccino): ")


    if choice == "report" :
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")
        coffeeMachine()

    insertCoins()

    coffee_cost = MENU[choice]['cost']
    coffee_water = MENU[choice]['ingredients']['water']
    coffee_milk = MENU[choice]['ingredients']['milk']
    coffee_coffee = MENU[choice]['ingredients']['coffee']

    if (total >= coffee_cost) and (water >= coffee_water) and (milk >= coffee_milk) and (coffee >= coffee_coffee):
        water -= coffee_water
        milk -= coffee_milk
        coffee -= coffee_coffee
        money += coffee_cost
        change = total - coffee_cost
        print(f"Here is ${change} in change.\nHere is your {choice} Enjoy!")

    elif total < coffee_cost:
        print("Sorry there is not enough money. Money refunded.")

    elif water < coffee_water:
        print("Sorry there is not enough water.")

    elif milk < coffee_milk:
        print("Sorry there is not enough milk.")

    elif coffee < coffee_coffee:
        print("Sorry there is not enough coffee.")

    coffeeMachine()

coffeeMachine()