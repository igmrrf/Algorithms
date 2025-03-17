from util import time_it


@time_it
def bubble_sort(nums: list[int]):
    # go through the array
    # check if the index is less than the next
    # if so, swap
    # else move to the next
    times = 0
    size = len(nums) - 1
    for j in range(size):
        swapped = False
        for i in range(size - j):
            times += 1
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
            else:
                continue
        if not swapped:
            break
    print(times)
    return nums


@time_it
def key_bubble_sort(elements, key):
    size = len(elements) - 1
    for j in range(size):
        swapped = False
        for i in range(size - j):
            if elements[i][key] > elements[i + 1][key]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swapped = True
            else:
                continue
        if not swapped:
            break


elements = [
    {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
    {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
    {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
    {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
]
nums = [38, 9, 29, 7, 50, 98, 2, 15, 28, 80]
bubble_sort(nums)
key_bubble_sort(elements, "name")
print(elements)
print(nums)
