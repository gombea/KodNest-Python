number=int(input())
total = 0
positive_count=0
negative_count=0
neutral_count=0
for i in range(number):
    n=int(input())
    total+=n
    if n> 0:
        positive_count += 1
    elif n < 0:
        negative_count += 1
    else:
        neutral_count += 1

print("Positive Count:", positive_count)
print("Negative Count:", negative_count)
print("Neutral Count:", neutral_count)
print("Total:",total)