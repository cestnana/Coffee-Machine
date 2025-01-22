# Coffee Machine Program TODOs

## Core Functionality
- [x] Implement main program loop with user prompt
  - [x] Prompt: "What would you like? (espresso/latte/cappuccino):"
  - [x] Show prompt after each completed action
  - [x] Handle user input validation

- [x] Implement machine shutdown
  - [x] Secret command: "off"
  - [x] End program execution when triggered

- [x] Create reporting system
  - [x] Command: "report"
  - [x] Display current resources:
    - [x] Water (ml)
    - [x] Milk (ml)
    - [x] Coffee (g)
    - [x] Money ($)

## Resource Management
- [x] Implement resource checking system
  - [x] Check if enough resources for selected drink
  - [x] Display appropriate error messages for insufficient resources
  - Track resources:
    - [x] Water
    - [x] Milk
    - [x] Coffee

## Payment System
- [x] Implement coin processing
  - [x] Accept coin inputs:
    - [x] Quarters ($0.25)
    - [x] Dimes ($0.10)
    - [x] Nickels ($0.05)
    - [x] Pennies ($0.01)
  - [x] Calculate total money inserted

- [x] Implement transaction verification
  - [x] Check if inserted amount meets drink price
  - [x] Handle insufficient funds
    - [x] Display error message
    - [x] Refund money
  - [x] Process change
    - [x] Round to 2 decimal places
    - [x] Display change amount
  - [x] Update machine profit

## Drink Making
- [x] Implement drink preparation
  - [x] Deduct resources for selected drink
  - [x] Update resource levels
  - [x] Display success message ("Here is your {drink}. Enjoy!")

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