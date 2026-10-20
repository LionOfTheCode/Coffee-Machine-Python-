# Coffee Machine Python

Coffee Machine Python is a simple command-line coffee machine simulator written in Python.

This project was created as a learning project from Hyperskill. It focuses on practicing basic Python programming, object-oriented programming, user input handling, and state machine design.

## Project Objectives

The main goals of this project are:

- Learn Python fundamentals
- Practice object-oriented programming
- Understand how to design and use a state machine
- Work with user input in a command-line application
- Simulate resource management in a coffee machine

## Features

The coffee machine can:

- Sell different types of coffee
- Check whether enough resources are available
- Deduct resources after making coffee
- Refill water, milk, coffee beans, and disposable cups
- Show the current machine resources
- Withdraw collected money
- Exit the program safely

## Available Coffee Options

| Option | Coffee Type | Water | Milk | Coffee Beans | Cups | Cost |
|---|---|---:|---:|---:|---:|---:|
| 1 | Espresso | 250 ml | 0 ml | 16 g | 1 | $4 |
| 2 | Latte | 350 ml | 75 ml | 20 g | 1 | $7 |
| 3 | Cappuccino | 200 ml | 100 ml | 12 g | 1 | $6 |

## Initial Machine Resources

| Resource | Amount |
|---|---:|
| Water | 400 ml |
| Milk | 540 ml |
| Coffee beans | 120 g |
| Disposable cups | 9 |
| Money | $550 |

## How to Run

Make sure Python is installed on your computer.

Run the program from the project directory:

    python main.py

Depending on your system, you may need to use:

    python3 main.py

## How to Use

After starting the program, the machine asks you to choose an action:

    Write action (buy, fill, take, remaining, exit):

Available actions:

| Action | Description |
|---|---|
| `buy` | Buy a coffee |
| `fill` | Add resources to the machine |
| `take` | Take all money from the machine |
| `remaining` | Show current machine resources |
| `exit` | Stop the program |

## Buying Coffee

Choose the `buy` action:

    buy

Then select a coffee type:

    What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:

Coffee options:

- `1` — espresso
- `2` — latte
- `3` — cappuccino
- `back` — return to the main menu

If the machine has enough resources, it will make the coffee:

    I have enough resources, making you a coffee!

If there are not enough resources, it will show a message like:

    Sorry, not enough water!

## Filling the Machine

Choose the `fill` action:

    fill

The program will ask how much of each resource you want to add:

    Write how many ml of water you want to add:
    Write how many ml of milk you want to add:
    Write how many grams of coffee beans you want to add:
    Write how many disposable cups you want to add:

## Checking Remaining Resources

Choose the `remaining` action:

    remaining

Example output:

    The coffee machine has:
    400 ml of water
    540 ml of milk
    120 g of coffee beans
    9 disposable cups
    $550 of money

## Taking Money

Choose the `take` action:

    take

Example output:

    I gave you $550

After this action, the machine money becomes `$0`.

## Exiting the Program

Choose the `exit` action:

    exit

The program will stop.

## Project Structure

    Coffee-Machine-Python-
    ├── main.py
    └── README.md

## Technologies Used

- Python
- Object-Oriented Programming
- Enum
- Command-line interface

## What I Learned

During this project, I practiced:

- Creating classes in Python
- Using methods to separate program logic
- Managing object state
- Working with enums
- Handling user input
- Designing a simple state machine
- Simulating real-world resource management

## Future Improvements

Possible improvements for this project:

- Add unit tests
- Add input validation for numeric values
- Store coffee recipes in a separate data class
- Add more coffee types
- Improve formatting of machine status output

## License

This project is for learning purposes.