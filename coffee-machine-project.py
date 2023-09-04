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
def is_resources(orderingredients):
    is_enough = True
    for item in orderingredients:
        if orderingredients[item] >= resources[item]:
            print("sorry not enough water")
            is_enough = False
    return is_enough
def process_coins():
    """return the total number of coins"""
    print("insert the coins")
    total = int(input("how many quarter")) * 0.25
    total += int(input("how many dimes")) * 0.1
    total += int(input("how many nickles")) * 0.05
    total += int(input("how many pennies")) * 0.01
    return total
def make_coffee(drink_name,orderingredients):
   """deduct the ingredients requirement from the resources"""
   for item in orderingredients:
       resources[item] -= orderingredients[item]

   print(f"here is your {drink_name} ☕")
def is_transaction_successfull(money_recived,drink_cost):
    """return the user money to purchase they selected"""
    if money_recived >= drink_cost:
        changed =round(money_recived - drink_cost,2)
        print(f"here is many added in {changed} changes")
        global profit
        profit += drink_cost
        return True
    else:
        return False
is_on = True
while is_on:
   choice = input("what you want to choose (espresso/latte/cappuccino)")
   if choice == "off":
      is_on = False
   elif choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk:{resources['milk']} ml")
       print(f"Coffee:{resources['coffee']} g")
       print(f"Money: {profit}")
   else:
       drink = MENU[choice]
       if is_resources(drink['ingredients']):
           payment = process_coins()
           is_transaction_successfull(payment,drink['cost'])
           make_coffee(choice,drink['ingredients'])
