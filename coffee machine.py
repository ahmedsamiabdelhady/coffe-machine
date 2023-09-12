import time
import os
import sys
sys.path.append('C:\\Users\\Sami\\Desktop')
from MENU import MENU, resources

def clear():
    os.system("cls")

def coins_process(n1, n2, n3, n4):
    return n1 * 0.01 + n2 * 0.05 + n3 * 0.1 + n4 * 0.25

def report(n):
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney:{n}$"

def check_resources(n1, n2):
    if resources['water'] < n1['water']:
        print("Sorry there is not enough water.")
        time.sleep(6)
        clear()
        return False
    elif n2 != "espresso" and resources['milk'] < n1['milk']:
        print("Sorry there is not enough milk.")
        time.sleep(6)
        clear()
        return False
    elif resources['coffee'] < n1['coffee']:
        print("Sorry there is not enough coffee.")
        time.sleep(6)
        clear()
        return False
    else:
        return True
    
def check_transaction(inserted, n):
    if inserted < n['cost']:
        print("sorry there`s no enough money.")
        time.sleep(6)
        clear()
    elif inserted > n['cost']:
        change = round(inserted - n['cost'], 2)
        print(f"Take {change}$ as a chnage")
        return True
    else:
        return True

def make_coffee(n1, n2):
    resources['water'] = resources['water'] - n1['water']
    if n2 != "espresso":
        resources['milk'] = resources['milk'] - n1['milk']
    resources['coffee'] = resources['coffee'] - n1['coffee']

def a_money(n1, n2):
    return n1 + n2['cost']

def coffee_machine():
    money = 0
    making_coffee = True
    while making_coffee:
        print("""
 ██████  ██████  ███████ ███████ ███████ ███████     ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
██      ██    ██ ██      ██      ██      ██          ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
██      ██    ██ █████   █████   █████   █████       ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
██      ██    ██ ██      ██      ██      ██          ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
 ██████  ██████  ██      ██      ███████ ███████     ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 
""")
        choose = input("what would you like? (espresso/latte/cappuccino):").lower()
        if choose == "report":
            print(report(money))
            time.sleep(6)
            clear()
        elif choose == "off":
            making_coffee = False
        else:
            item = MENU[f'{choose}']
            nums = item['ingredients']
            print(f"{item['cost']}$")
            if check_resources(nums, choose) == True:
                print("insert money")
                pennies = int(input("How much pennies: "))
                nickles = int(input("How much nickles: "))
                dimes = int(input("How much dimes: "))
                quarters = int(input("How much quarters: "))
                inserted_money = coins_process(pennies, nickles, dimes, quarters)
                
                if check_transaction(inserted_money, item) == True:
                    money = a_money(money, item)
                    make_coffee(nums, choose)
                    print(
"""
         {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--.
   |            (__  \
   |             | )  )
   |             |/  /
   |             /  /    -Ahmed Sami-
   |            (  /
   \             y'
    `-.._____..-'
""")
                    print(f"enjoy with your {choose}!")
                    time.sleep(6)
                    clear()

coffee_machine()











