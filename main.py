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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resource_sufficient(order_ingredients):
  """ Returns true is sufficient ingredients in machine """
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"Sorry there is not enough {item}")
      return False
  return True

def process_coins():
  print("Please insert coins")
  total = int(input("how manu quarters?")) * 0.25
  total += int(input("how manu dimes?")) * 0.1
  total += int(input("how manu nickles?")) * 0.05
  total += int(input("how manu pennys?")) * 0.01
  return total


def is_transaction_successful(amountreceived,costofdrink):
  """returns true if payment succesfull, false otherwise"""
  global profit
  if costofdrink <= amountreceived:
    profit += costofdrink
    change = round(amountreceived - costofdrink,2)
    print(f"here is your change $: {change}")
    return True
  else:
    print ("sorry that is not enough money, here is your refund")
    return False


def make_coffee(drinkname,orderingredients):
  """deducts ingredients from stock"""
  for item in orderingredients:
    resources[item] -= orderingredients[item]
  print(f"Here is your {drinkname}")

is_on = True


while is_on:
  choice = input("What would you like? espresso/latte/cappuccino \n") 
  if choice == "off":
    is_on = False
  elif choice == "report":
    for key in resources:
      print(key,":",resources[key])
    print(f"Profit: ${profit}")
  else:
    drink = MENU[choice]
    if is_resource_sufficient(drink["ingredients"]):
      payment = process_coins()
      if is_transaction_successful(payment,drink["cost"]):
        make_coffee(choice,drink["ingredients"])
