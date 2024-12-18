# Coffee Machine Program TODOs

## Core Functionality
- [x] Implement main program loop with user prompt
  - Prompt: "What would you like? (espresso/latte/cappuccino):"
  - Show prompt after each completed action
  - Handle user input validation

- [x] Implement machine shutdown
  - Secret command: "off"
  - End program execution when triggered

- [x] Create reporting system
  - Command: "report"
  - Display current resources:
    - Water (ml)
    - Milk (ml)
    - Coffee (g)
    - Money ($)

## Resource Management
- [x] Implement resource checking system
  - Check if enough resources for selected drink
  - Display appropriate error messages for insufficient resources
  - Track resources:
    - Water
    - Milk
    - Coffee

## Payment System
- [x] Implement coin processing
  - Accept coin inputs:
    - Quarters ($0.25)
    - Dimes ($0.10)
    - Nickels ($0.05)
    - Pennies ($0.01)
  - Calculate total money inserted

- [x] Implement transaction verification
  - Check if inserted amount meets drink price
  - Handle insufficient funds
    - Display error message
    - Refund money
  - Process change
    - Round to 2 decimal places
    - Display change amount
  - Update machine profit

## Drink Making
- [x] Implement drink preparation
  - Deduct resources for selected drink
  - Update resource levels
  - Display success message ("Here is your {drink}. Enjoy!")

## Drink Recipes
- [x] Define drink requirements
  ### Latte
  - [x] Water: 200ml
  - [x] Milk: 150ml
  - [x] Coffee: 24g
  - [x] Price: $2.50

  ### Espresso
  - [x] Water: 50ml
  - [x] Coffee: 18g
  - [x] Price: $1.50

  ### Cappuccino
  - [x] Water: 250ml
  - [x] Milk: 100ml
  - [x] Coffee: 24g
  - [x] Price: $3.00

## Testing
- [x] Test all user interactions
- [x] Verify resource management
- [x] Test payment processing
- [x] Validate drink making process