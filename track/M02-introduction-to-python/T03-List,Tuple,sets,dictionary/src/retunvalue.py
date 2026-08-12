

def calcualte(first_number,second_number,operator):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    else:
        return first_number/ second_number


first_number=input()
second_number=input()
operator=input()
x = calcualte(first_number,second_number,operator)
print(x)