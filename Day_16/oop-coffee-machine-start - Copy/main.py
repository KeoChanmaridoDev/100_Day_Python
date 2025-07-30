from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


"""USER INPUT """
# THIS CALL OBJECT=CLASS
my_coffee = CoffeeMaker()

menu = Menu()
my_money_machine = MoneyMachine()
# THIS CALL OBJECT.METHOD


is_on = True
while is_on:
    options = menu.get_items()
    choice  = input(f"Which option would you like to choose? ({options}): ")
    if choice not in ("latte", "espresso", "cappuccino", "report", "off"):
        print("Please enter a valid option.")
        continue
    elif choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffee.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee.make_coffee(drink)

