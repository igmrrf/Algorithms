from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    # array of results of sum of array
    size = len(nums)
    answer = [1] * size
    left = 1
    for i in range(size):
        answer[i] *= left
        left *= nums[i]

    right = 1
    for i in range(size - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer


print(productExceptSelf([1, 2, 3, 4, 5]))
