import random

from util import time_it


# @time_it
# def insertion_sort(elements):
#     sorted_elements = []
#     for i in range(len(elements)):
#         left = 0
#         while left < i:
#             if sorted_elements[left] < elements[i]:
#                 left += 1
#             else:
#                 break
#         sorted_elements.insert(left, elements[i])


# @time_it
# def insertion_sort(elements):
#     for i in range(1, len(elements)):
#         left = 0
#         while left < i:
#             if elements[left] <= elements[i]:
#                 left += 1
#             else:
#                 break
#
#         elements[0:] = (
#             elements[:left] + [elements[i]] + elements[left:i] + elements[i + 1 :]
#         )
#     return elements
#
#
@time_it
def insertion_sort(elements):
    for i in range(1, len(elements)):
        value = elements[i]
        left = i - 1
        while left >= 0 and elements[left] > value:
            elements[left + 1] = elements[left]
            left -= 1

        elements[left + 1] = value


nums = [3, 1, 9, 20, 3]

for i in range(10000):
    nums.append(random.randint(1, 10000))

insertion_sort(nums)
# print(nums)
