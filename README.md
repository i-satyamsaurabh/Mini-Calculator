# Mini-Calculator-

def perform_calculation():
    print("Hello, You're Welcome!")
    f = int(input("Enter your First Number: "))
    o = input("Enter your Operator from (+, -, *, /, %): ")
    s = int(input("Enter your Second Number: "))

    if o == "+":
        result = f + s
    elif o == "-":
        result = f - s
    elif o == "*":
        result = f * s
    elif o == "/":
        result = f / s
    elif o == "%":
        result = f % s
    else:
        print("Invalid Operation")
        return

    print("Your output is", result)

# Call the function to execute the code
perform_calculation()
