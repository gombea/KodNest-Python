def check_prime(num):
    for num in range(2,num-1):
        if num % 2 != 0:
            print("notPrime")
            return False
        else:
            print("Prime")
            return True




num = int(input("Enter a number"))
result = check_prime(num)
print(result)