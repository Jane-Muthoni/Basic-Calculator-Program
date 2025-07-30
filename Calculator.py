num1 = 50
num2 = 15  
operation = "+" 

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation! Please enter +, -, * or /")
