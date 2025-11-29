# Coffee Machine Program TODOs

## Core Functionality
- Implement main program loop with user prompt
  - [*] Prompt: "What would you like? (espresso/latte/cappuccino):"
  - [*] Show prompt after each completed action
  - [*] Handle user input validation

- Implement machine shutdown
  - [*] Secret command: "off"
  - [*] End program execution when triggered

- Create reporting system
  - [*] Command: "report"
  - Display current resources:
    - [*] Water (ml)
    - [*] Milk (ml)
    - [*] Coffee (g)
    - [*] Money ($)

## Resource Management
- Implement resource checking system
  - [*] Check if enough resources for selected drink
  - [*] Display appropriate error messages for insufficient resources
  - [*] Track resources:
    - [*] Water
    - [*] Milk
    - [*] Coffee

## Payment System
- Implement coin processing
  - Accept coin inputs:
    - [*] Quarters ($0.25)
    - [*] Dimes ($0.10)
    - [*] Nickels ($0.05)
    - Pennies ($0.01)
  - Calculate total money inserted

- Implement transaction verification
  - Check if inserted amount meets drink price
  - Handle insufficient funds
    - Display error message
    - Refund money
  - Process change
    - Round to 2 decimal places
    - Display change amount
  - Update machine profit

## Drink Making
- Implement drink preparation
  - Deduct resources for selected drink
  - Update resource levels
  - Display success message ("Here is your {drink}. Enjoy!")

## Drink Recipes
- Define drink requirements
  ### Latte
  - Water: 200ml
  - Milk: 150ml
  - Coffee: 24g
  - Price: $2.50

  ### Espresso
  - Water: 50ml
  - Coffee: 18g
  - Price: $1.50

  ### Cappuccino
  - Water: 250ml
  - Milk: 100ml
  - Coffee: 24g
  - Price: $3.00

## Testing
- Test all user interactions
- Verify resource management
- Test payment processing
- Validate drink making process