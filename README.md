# Coffee Machine Simulator

A command-line interface program that simulates a coffee machine with various drink options and coin operations.

## Description

This program simulates a coffee machine that can make three types of drinks: espresso, latte, and cappuccino. It manages resources like water, milk, and coffee, handles monetary transactions with coins, and provides reporting functionality.

## Features

- Multiple drink options (espresso/latte/cappuccino)
- Resource management (water, milk, coffee)
- Coin processing system (accepts quarters, dimes, nickles, pennies)
- Real-time resource tracking
- Maintenance mode with reporting functionality
- Change calculation and dispensing

## Usage

When running the program, you can:

1. Order drinks by selecting from the menu
2. Check machine resources by typing "report"
3. Insert coins when prompted
4. Receive change if overpaid
5. Turn off machine using "off" command

### Available Commands

- `espresso`: Order an espresso
- `latte`: Order a latte
- `cappuccino`: Order a cappuccino
- `report`: View current resource levels
- `off`: Turn off the machine

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
```bash
git clone [your-repository-url]
```

2. Navigate to the project directory:
```bash
cd coffee-machine
```

3. Run the program:
```bash
python main.py
```

