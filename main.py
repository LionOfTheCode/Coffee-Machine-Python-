# Usage per portion
WATER_PER_PORTION = 200
MILK_PER_PORTION = 50
COFFEE_PER_PORTION = 15

COFFEE_RECIPES = {
    "1": {
        "name": "espresso",
        "water": 250,
        "milk": 0,
        "coffee": 16,
        "cost": 4
    },
    "2": {
        "name": "latte",
        "water": 350,
        "milk": 75,
        "coffee": 20,
        "cost": 7
    },
    "3": {
        "name": "cappuccino",
        "water": 200,
        "milk": 100,
        "coffee": 12,
        "cost": 6
    }
}


def print_machine_status(machine_content):
    """Function to display the current status of the coffee machine."""

    print("The coffee machine has:")
    print(f"{machine_content['water']} ml of water")
    print(f"{machine_content['milk']} ml of milk")
    print(f"{machine_content['coffee']} g of coffee beans")
    print(f"{machine_content['cups']} disposable cups")
    print(f"${machine_content['money']} of money")


def buy_coffee(machine_content):
    """
    Function to buy coffee from the machine. Takes machine content as argument.
    According to the coffee type, reduces machine content from provided machine content.
    Returns nothing.
    """

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = input()
    recipe = COFFEE_RECIPES[coffee_type]
    machine_content["water"] -= recipe["water"]
    machine_content["milk"] -= recipe["milk"]
    machine_content["coffee"] -= recipe["coffee"]
    machine_content["money"] += recipe["cost"]
    machine_content["cups"] -= 1
    print()


def fill_machine(machine_content):
    # TODO Implement filling the machine with resources, UI and business logic are still mixed
    """
    Function to fill the coffee machine with resources. Takes machine content as argument.
    Adds specified amounts of water, milk, coffee beans, and disposable cups to the machine content.
    Returns nothing.
    """
    print("Write how many ml of water you want to add:")
    machine_content["water"] += int(input())
    print("Write how many ml of milk you want to add:")
    machine_content["milk"] += int(input())
    print("Write how many grams of coffee beans you want to add:")
    machine_content["coffee"] += int(input())
    print("Write how many disposable cups you want to add:")
    machine_content["cups"] += int(input())
    print()


def withdraw_money(machine_content):
    """Function to withdraw money from the machine. Takes machine content as argument. Returns nothing."""
    print(f"I gave you {machine_content['money']}")
    machine_content["money"] = 0
    print()


def main():
    machine_content = {
        "water": 400,
        "milk": 540,
        "coffee": 120,
        "cups": 9,
        "money": 550
    }

    print_machine_status(machine_content)
    print("Write action (buy, fill, take):")
    action = input()

    if action == "buy":
        buy_coffee(machine_content)
    elif action == "fill":
        fill_machine(machine_content)
    elif action == "take":
        withdraw_money(machine_content)
    else:
        pass
        # print("Invalid action. Please choose 'buy', 'fill', or 'take'.")

    print_machine_status(machine_content)


if __name__ == "__main__":
    main()
