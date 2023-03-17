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


def report_resources():
    """Imprime o relatório de recursos"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}ml')
    print(f'Money: ${profit}')


def check_sufficient_resources(order_ingredients):
    """Verifica se há recursos suficientes"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def is_transaction_sucessfull(menu_cost, monetary_value):
    """Retorna True se o pagamento é aceito or False se o dinheiro é insuficiente"""
    return menu_cost <= monetary_value


def reduce_resources(coffee):
    """Reduz os recursos"""
    for item in MENU[coffee]["ingredients"]:
        resources[item] -= MENU[coffee]["ingredients"][item]


is_machine_on = True
while is_machine_on:
    coffee_type = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if coffee_type not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
        print('invalid option')
    elif coffee_type == 'report':
        report_resources()
    elif coffee_type == 'off':
        is_machine_on = False
    else:
        print(f'Custo do {coffee_type} é {MENU[coffee_type]["cost"]}')
        print('please insert coins')
        total = int(input('How many quarters (0.25): ')) * 0.25
        total += int(input('How many dimes (0.10): ')) * 0.10
        total += int(input('How many nickles (0.05): ')) * 0.05
        total += int(input('How many pennies (0.01): ')) * 0.01

        if check_sufficient_resources(MENU[coffee_type]["ingredients"]):
            if not is_transaction_sucessfull(MENU[coffee_type]["cost"], total):
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit = MENU[coffee_type]["cost"]
                change_value = round(abs(total - profit),2)

                if change_value > 0:
                    print(f"Here is ${change_value} in change")

                reduce_resources(coffee_type)
                print(f"Here is {coffee_type}. Enjoy!")



# Program requirements
# 1. Print report
# 2. Check resources sufficient ?
# 3. Process coins
# 4. Check transaction successful ?
# 5. Make Coffe
# Penny => 1 centavo
# Nickel => 5 centavos
# Dime => 10 centavos
# Quarter => 25 centavos
