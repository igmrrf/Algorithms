# def sum_two_smallest_numbers(numbers):
#     # sort numbers smallest to largest
#     # add first two
#     sorted = []
#     for numb in numbers:
#         if len(sorted) < 2:
#             if len(sorted):
#                 if sorted[0] > numb:
#                     sorted[1] = sorted[0]
#                     sorted[0] = numb
#                 sorted.append(numb)
#             else: sorted.append(numb)
#         else:
#             if numb < sorted[0]:
#                 sorted[1] = sorted[0]
#                 sorted[0] = numb
#             elif numb < sorted[1]:
#                 sorted[1] = numb
#     print(sorted)
#     return sorted[0] + sorted[1]

def sum_two_smallest_numbers(numbers):
    print(sum(sorted(numbers)[:2]))
    
    return numbers[0] + numbers[1]



print(sum_two_smallest_numbers([4,9,1,8,47,2]))

