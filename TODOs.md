# Coffee Machine Program TODOs

## Core Functionality
- [ ] Implement main program loop with user prompt
  - Prompt: "What would you like? (espresso/latte/cappuccino):"
  - Show prompt after each completed action
  - Handle user input validation

- [ ] Implement machine shutdown
  - Secret command: "off"
  - End program execution when triggered

- [ ] Create reporting system
  - Command: "report"
  - Display current resources:
    - Water (ml)
    - Milk (ml)
    - Coffee (g)
    - Money ($)

## Resource Management
- [ ] Implement resource checking system
  - Check if enough resources for selected drink
  - Display appropriate error messages for insufficient resources
  - Track resources:
    - Water
    - Milk
    - Coffee