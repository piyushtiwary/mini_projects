from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
	menu_list = menu.get_items()
	user = input(f"What would you like to get: {menu_list} or enter off to exit")

	if user == "off":
		is_on = False

	elif user == "report":
		money_machine.report()
		coffee_maker.report()
		
	else:
		order = menu.find_drink(user)
		if coffee_maker.is_resource_sufficient(order):
			if money_machine.make_payment(order.cost):
				coffee_maker.make_coffee(order)

	
	



