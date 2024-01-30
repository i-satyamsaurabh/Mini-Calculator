# Mini-Calculator-

The provided code defines a simple calculator function named `perform_calculation()`. Here's a description of the code:

1. The function starts by printing a welcoming message: "Hello, You're Welcome!"

2. It then prompts the user to input their first number (`f`), an operator (`o`) from the set (+, -, *, /, %), and their second number (`s`).

3. The code uses an `if-elif-else` structure to perform the corresponding arithmetic operation based on the provided operator:
   - If the operator is '+', it adds the first and second numbers.
   - If the operator is '-', it subtracts the second number from the first.
   - If the operator is '*', it multiplies the first and second numbers.
   - If the operator is '/', it divides the first number by the second.
   - If the operator is '%', it calculates the remainder when dividing the first number by the second.

4. If the provided operator is not one of the specified operators (+, -, *, /, %), it prints "Invalid Operation" and returns from the function.

5. If a valid operation is performed, it prints the result: "Your output is [result]".

6. The code concludes by calling the `perform_calculation()` function, allowing the user to execute the calculator by providing input.

Overall, this code defines a basic calculator that takes two numbers and an operator as input, performs the specified operation, and displays the result.
