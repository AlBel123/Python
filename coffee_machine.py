import data
print(data.pic)

def coffee_choice():
    """This function returns the choice of the drink"""
    
    drink=input("\nWhat would you like? espresso/latte/cappuccino: ").lower()
    if drink=="espresso":
        check_resources(drink)
        return "espresso" 
    elif drink=="latte":
        check_resources(drink)
        return "latte"
    elif drink=="cappuccino":
        check_resources(drink)
        return "cappuccino"
    
    #report does not work after the function implementation...
    elif drink=="report":
        water=data.resources["water"]
        milk=data.resources["milk"]
        coffee=data.resources["coffee"]
        print (f"Water: {water} ml\nMilk: {milk} ml\nCoffee: {coffee} ml\n")
        coffee_choice()
    
    elif drink=="off":
        exit()
    else:
        print("Pleae make your choice")
        coffee_choice()



def check_resources(drink):
    """Returns warning in the case if the resources are not sufficient for the Drink"""

    water_availability=data.resources["water"]-data.MENU[drink]["ingredients"]["water"]
    milk_availability=data.resources["milk"]-data.MENU[drink]["ingredients"]["milk"]
    coffee_availability=data.resources["coffee"]-data.MENU[drink]["ingredients"]["coffee"]

    if water_availability<=0:
        print("Sorry, there is not enough Water...")
        coffee_choice()
    if coffee_availability<=0:
        print("Sorry, there is not enough Coffee...")
        coffee_choice()
    if milk_availability<=0:
        print("Sorry, there is not enough Milk...") 
        coffee_choice()
    else:
        process_coins(drink)


def process_coins(drink):
    """Returns warning and refunds money if non sufficient for the drink and brings back to the coffee choice. If the sum is enough - prepare coffe, update the report and gives change"""
    print("PLease insert you coins")
    quarters=int(input("how many Quarters you insert?: "))
    dimes=int(input("how many Dimes you insert?: "))
    nickles=int(input("how many Nickels you insert?: "))
    pennies=int(input("how many Pennies you insert?: "))
    sum_inserted=float(quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01)
    if sum_inserted-data.MENU[drink]["cost"]<0:
        print("Sorry that's not enough money. Money refunded.")
        
    else:
        data.resources["water"]-=data.MENU[drink]["ingredients"]["water"]
        data.resources["milk"]-=data.MENU[drink]["ingredients"]["milk"]
        data.resources["coffee"]-=data.MENU[drink]["ingredients"]["coffee"]
        data.resources["money"]+=data.MENU[drink]["cost"]
        # print(data.resources)
        if sum_inserted-data.MENU[drink]["cost"]>0:
            print(f"Your change is {round((sum_inserted-data.MENU[drink]['cost']),2)}")
        print(f"Enjoy your {drink}!")
    coffee_choice()




coffee_choice()

# def make_coffee(drink):
#     """Changes the data in Report, gives Coffee and Change"""