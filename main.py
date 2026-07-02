from enum import Enum


class CoffeeMachine:
    # TODO Improve coffee recipes. Probably as DataClass?
    COFFEE_RECIPES = {
        "1": {
            "name": "espresso",
            "water": 250,
            "milk": 0,
            "coffee": 16,
            "cups": 1,
            "cost": 4
        },
        "2": {
            "name": "latte",
            "water": 350,
            "milk": 75,
            "coffee": 20,
            "cups": 1,
            "cost": 7
        },
        "3": {
            "name": "cappuccino",
            "water": 200,
            "milk": 100,
            "coffee": 12,
            "cups": 1,
            "cost": 6
        }
    }

    class State(Enum):
        CHOOSING_ACTION = "choosing_action"
        CHOOSING_COFFEE = "choosing_coffee"
        FILLING_WATER = "filling_water"
        FILLING_MILK = "filling_milk"
        FILLING_COFFEE = "filling_coffee"
        FILLING_CUPS = "filling_cups"
        EXIT = "exit"

    def __init__(self, water=400, milk=540, coffee=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.state = CoffeeMachine.State.CHOOSING_ACTION

    def is_running(self):
        """Returns True if the coffee machine is still running."""
        return self.state != CoffeeMachine.State.EXIT

    def user_prompt(self):
        """Returns the prompt for the user based on the current state."""
        if self.state == CoffeeMachine.State.CHOOSING_ACTION:
            return "Write action (buy, fill, take, remaining, exit):\n"
        elif self.state == CoffeeMachine.State.CHOOSING_COFFEE:
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"
        elif self.state == CoffeeMachine.State.FILLING_WATER:
            return "Write how many ml of water you want to add:\n"
        elif self.state == CoffeeMachine.State.FILLING_MILK:
            return "Write how many ml of milk you want to add:\n"
        elif self.state == CoffeeMachine.State.FILLING_COFFEE:
            return "Write how many grams of coffee beans you want to add:\n"
        elif self.state == CoffeeMachine.State.FILLING_CUPS:
            return "Write how many disposable cups you want to add:\n"

    def handle_input(self, user_input):
        """Statemachine core. Handles user input"""

        if self.state == CoffeeMachine.State.CHOOSING_ACTION:
            return self._handle_action(user_input)
        elif self.state == CoffeeMachine.State.CHOOSING_COFFEE:
            return self._handle_coffee_choice(user_input)
        elif self.state == CoffeeMachine.State.FILLING_WATER:
            self._handle_fill_water(user_input)
        elif self.state == CoffeeMachine.State.FILLING_MILK:
            self._handle_fill_milk(user_input)
        elif self.state == CoffeeMachine.State.FILLING_COFFEE:
            self._handle_fill_beans(user_input)
        elif self.state == CoffeeMachine.State.FILLING_CUPS:
            self._handle_fill_cups(user_input)
        return None

    def _handle_action(self, user_input):
        """Handle user action."""
        if user_input == "buy":
            self.state = CoffeeMachine.State.CHOOSING_COFFEE
        elif user_input == "fill":
            self.state = CoffeeMachine.State.FILLING_WATER
        elif user_input == "take":
            return self._withdraw_money()
        elif user_input == "remaining":
            return self._get_machine_status()
        elif user_input == "exit":
            self.state = CoffeeMachine.State.EXIT
            return None
        return None

    def _find_missing_resource(self, recipe):
        """Return the name of the first missing resource, or None."""
        if self.water < recipe["water"]:
            return "water"
        if self.milk < recipe["milk"]:
            return "milk"
        if self.coffee < recipe["coffee"]:
            return "coffee"
        if self.cups < recipe["cups"]:
            return "disposable cups"
        return None

    def _handle_coffee_choice(self, choice):
        """Interpret the user's coffee selection and make the drink
        if resources are sufficient."""
        if choice == "back":
            self.state = CoffeeMachine.State.CHOOSING_ACTION
            return None

        recipe = CoffeeMachine.COFFEE_RECIPES.get(choice)
        if recipe is None:
            self.state = CoffeeMachine.State.CHOOSING_ACTION
            return None

        missing = self._find_missing_resource(recipe)
        if missing is not None:
            self.state = CoffeeMachine.State.CHOOSING_ACTION
            return f"Sorry, not enough {missing}!\n"

        # Deduct resources and collect payment
        self.water -= recipe["water"]
        self.milk -= recipe["milk"]
        self.coffee -= recipe["coffee"]
        self.cups -= recipe["cups"]
        self.money += recipe["cost"]

        self.state = CoffeeMachine.State.CHOOSING_ACTION
        return "I have enough resources, making you a coffee!\n"

    # Machine filling
    """Handles filling the machine with water, milk, coffee, and cups. takes int from user"""

    def _handle_fill_water(self, user_input):
        self.water += int(user_input)
        self.state = CoffeeMachine.State.FILLING_MILK

    def _handle_fill_milk(self, user_input):
        self.milk += int(user_input)
        self.state = CoffeeMachine.State.FILLING_COFFEE

    def _handle_fill_beans(self, user_input):
        self.coffee += int(user_input)
        self.state = CoffeeMachine.State.FILLING_CUPS

    def _handle_fill_cups(self, user_input):
        self.cups += int(user_input)
        self.state = CoffeeMachine.State.CHOOSING_ACTION

    def _get_machine_status(self):
        """Returns the current status of the coffee machine."""

        return f"""The coffee machine has:
        {self.water} ml of water
        {self.milk} ml of milk
        {self.coffee} g of coffee beans
        {self.cups} disposable cups
        ${self.money} of money \n"""

    def _withdraw_money(self):
        """Returns collected money from the machine."""

        money_withdrawn = self.money
        self.money = 0
        return f"I gave you ${money_withdrawn}\n"


def main():
    coffee_machine = CoffeeMachine()
    response = None
    while coffee_machine.is_running():
        response = coffee_machine.handle_input(input(coffee_machine.user_prompt()))
        if response:
            print(response)
            response = None


if __name__ == "__main__":
    main()
