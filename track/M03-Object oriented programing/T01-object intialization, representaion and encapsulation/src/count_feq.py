def count_freq(str,target):
    count = 0
    for char in str:
         if char == target:
          count += 1
          print(count)

count_freq("india", "i")