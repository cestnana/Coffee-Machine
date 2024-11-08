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

def print_report():
  """Prints current resource levels and money."""
  for item, amount in resources.items():
    if item == "coffee":
      print(f"{item.capitalize()}: {amount}g")
    else:
      print(f"{item.capitalize()}: {amount}ml")
  print(f"Money: ${profit:.2f}")

def check_resources(drink_name):
  """Check if there are sufficient resources to make the drink."""
  for item, amount in MENU[drink_name]["ingredients"].items():
    if resources[item] < amount:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

profit = 0

def coffee_machine():
  while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
      return
    elif choice == "report":
      print_report()
    elif choice in MENU:
      if check_resources(choice):
        # Payment processing and drink making will be added here later
        pass
    else:
      print("Invalid selection. Please try again.")

coffee_machine()
