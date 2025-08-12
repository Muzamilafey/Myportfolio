# muzamil mohamed
#simple calculator
result = 0
print("Welcome to the Simple Calculator!")
try:
    number1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /,^): ")
    number2 = float(input("Enter second number: "))
    if operation == "+":
        result = number1+number2
        print(f"{number1}{operation}{number2}={result}")
    elif operation == "-":
        result = number1-number2
        print(f"{number1}{operation}{number2}={result}")
    elif operation =="*":
        result = number1*number2
        print(f"{number1}{operation}{number2}={result}")
    elif operation =="/":
        if number2 == 0:
            print("Error (Division by zero)")
        else:
            result = number1/number2
            print(f"{number1}{operation}{number2}={result}")
    elif operation == "^":
        result = number1**number2
        print(f"{number1}{operation}{number2}={result}")
    else:
        print("syntax error(Invalid operator)")
    
except ValueError:
    print("invalid input. please enter a numeric value")
# End of calculator.py
# This is a simple calculator that performs basic arithmetic operations.