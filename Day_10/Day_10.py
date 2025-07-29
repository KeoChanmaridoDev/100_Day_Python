

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

var1 = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

continueOrNot = True
num1 = float(input("Enter first number: "))
while continueOrNot:

    for symsbol in var1:
        print(symsbol)
    operator = input("Please choice operations:")
    num2 = float(input("Enter second number: "))
    result = var1[operator](num1, num2)
    should_continue = input("Would you like to continue? (y/n): ").lower()
    if should_continue == "n":
        print(f"Your result is: {result}")
        continueOrNot = False
    else:
        num1 = result
