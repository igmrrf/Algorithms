numbers =[10,20,300,40,50]

# numbers[1]= "Adam"

# for num in numbers:
#     print(num)

# for i in range(len(numbers)):
#     print(numbers[i])
 
# print(numbers[-2:-1])

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)

