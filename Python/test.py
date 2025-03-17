from util import time_it


@time_it
def bubble_sort(nums: list[int]):
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


nums = [38, 9, 29, 7, 50, 98, 2, 15, 28, 80]
bubble_sort(nums)
print(nums)
