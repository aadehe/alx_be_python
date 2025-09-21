#Prompt for first Number
num1 = float(input("Enter the first number: "))

#Prompt for second Number
num2 = float(input("Enter the second number: "))

#Prompt for operation
operation = input("Choose the operation (+, -, *, /): ")

#Perform operation using match-case
match operation:
    case "+":
        print(f"The result is {num1 + num2}.")
    case "-":
        print(f"The result is{num1 - num2}.")
    case "*":
        print(f"The result is{num1 * num2}.")
    case "/":
        if num2 != 0:
            print(f"The result is{num1 / num2}.")
        else:
            print("Cannot divide by zero.")
    case _:
        result = "Invalid operation!"
