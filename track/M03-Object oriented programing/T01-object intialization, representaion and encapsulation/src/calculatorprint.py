def mini_calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "//":
        return num1 // num2
    else:
        return "Invalid operation"


num1 = int(input())
num2 = int(input())
operation = input()

result = mini_calculator(num1, num2, operation)
print(result)