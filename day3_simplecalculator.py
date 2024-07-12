def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

num1 = float(input("Enter first number: "))
operator = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    result = add(num1, num2)
    print(f"the sum of {num1} and {num2} is {result}")
elif operator == '-':
    result = subtract(num1, num2)
    print(f"the difference of {num1} and {num2} is {result}")
elif operator == '*':
    result = multiply(num1, num2)
    print(f"the product of {num1} and {num2} is {result}")
elif operator == '/':
    result = divide(num1, num2)
    print(f"the division of {num1} and {num2} is {result}")
else:
    print("INVALID OPERATOR")


