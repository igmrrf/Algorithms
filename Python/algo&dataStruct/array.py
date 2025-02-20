# Cant mix data types

# numbers = [10, 20, 30, 40, 8, 33];

numbers ='numbers'

print(numbers[::-1])

maximum = numbers[0]

# O(N) search running time
for num in numbers:
  if num > maximum:
    maximum = num
  
print(maximum)