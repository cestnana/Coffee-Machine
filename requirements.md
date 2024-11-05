Coffee Machine Program Requirements
1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):” 
    * Check the user’s input to decide what to do next. 
    * The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer. 
2. Turn off the Coffee Machine by entering “ off” to the prompt. 
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.Water: 100mlMilk: 50ml
        Coffee: 76g
        Money: $2.5
4. Check resources sufficient? 
    * When the user chooses a drink, the program should check if there are enough resources to make that drink. 
    * E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “ Sorry there is not enough water.” 
    * The same should happen if another resource is depleted, e.g. milk or coffee. 