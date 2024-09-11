from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker=CoffeeMaker()     # creating an objects
menu=Menu()
is_on=True                     # start with the statment for the loop
while is_on:
    print(f"hi there what would you like to drinf we have {menu.get_items()}")         # print options
    choice=input("what wold you like").lower()             #get user choice
    drink=menu.find_drink((choice))              # serch for drink in menu

    if choice=="report":                   # user need a report
        coffe_maker.report()
        money_machine.report()

    elif choice== "off":     # if user is swiching off
        is_on=False

    else:                   # we will check here all diffrent parameter
        if coffe_maker.is_resource_sufficient(drink):
            payment_anoff=money_machine.make_payment(drink.cost)
            if payment_anoff:
                coffe_maker.make_coffee(drink)


