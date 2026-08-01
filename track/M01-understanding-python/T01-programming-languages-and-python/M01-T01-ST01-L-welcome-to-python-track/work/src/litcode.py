s = input("Enter a string: ")

count = 0

for i in range(len(s) - 1, -1, -1):

    if s[i] != " ":
        count = count + 1

    elif count > 0:
        break

print("Length of last word =", count)