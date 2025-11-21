from os import MFD_ALLOW_SEALING

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

def is_resources_insufficient(ress):
    for item in ress:
        if ress[item]>resources[item]:
            print("Sorry you dont have enough resources")
            return False
    return True

def process_coins():
    total=0
    quater=int(input("Enter the number of quaters: "))
    dime=int(input("Enter the number of dimes: "))
    nickles=int(input("Enter the number of nickles: "))
    pennies=int(input("Enter the number of pennies: "))
    total+=quater*0.25+dime*0.10+nickles*0.05+pennies*0.01
    return total

def coins_sufficient(cost):
    if cost>amount:
        print("Sorry you dont have enough money, Money refunded")
        return False
    if cost<amount:
        print("Your refund: ",amount-cost,"$")
    return True

def enough_resources(things):
    for item in things:
        resources[item]-=things[item]

while True:
    choice=input("What would you like? Espresso/latte/cappuccino:").lower()
    if choice=="off":
        break
    elif choice=="report":
        print(f"water is {resources['water']}ml")
        print(f"Coffee is {resources['coffee']}g")
        print(f"Milk is {resources['milk']}ml")
        print(f"Money is {profit}")
    else:
        drink=MENU[choice]
        if is_resources_insufficient(drink["ingredients"]):
            print("Your total is 1.5")
            amount=process_coins()
            if coins_sufficient(drink["cost"]):
                profit+=drink["cost"]
                enough_resources(drink["ingredients"])
                print(f"Here is a {choice} enjoy!!")
