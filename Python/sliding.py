from typing import List
from time import time


#
# def fixed_sliding(nums: List[int], k: int):
#     if len(nums) < k:
#         raise ValueError("The length of nums must be at least k.")
#
#     k_sum = 0
# #     k_sum = sum(nums[:k])  # Initial window sum
#     for i in range(k):
#         k_sum += nums[i]
#
#     max_result = k_sum
#
#     for i in range(k, len(nums)):
#         k_sum += nums[i] - nums[i - k]
# #         max_result = max(max_result, k_sum)  # Update max if needed
#         if k_sum > max_result:
#             max_result = k_sum
#     return max_result
#
#
#
# nums1 = [2, 1, 5, 1, 3, 2]
# nums2 = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
#
#
# time1 = time()
# print(fixed_sliding(nums=nums1, k=3))
# print(fixed_sliding(nums2, 3))
# print(time() - time1)
#
#
#
# def dynamic_sliding(nums: List[int], k: int):
#     max_size = 0
#     window_sum = 0
#     left = 0
#
#     # go through
#     for right in range(len(nums)):
#         # set window to sum right element
#         window_sum += nums[right]
#
#         while window_sum > k:
#             print(window_sum, left)
#             window_sum -= nums[left]
#             left += 1
#         if len(nums[left : right + 1]) > max_size:
#             max_size = len(nums[left : right + 1])
#         # max_size = max(max_size, right - left + 1)
#
#     return max_size
#
#
# def longest_subarray_at_most_k(nums: List[int], k: int) -> int:
#     left = 0
#     curr_sum = 0
#     max_length = 0
#
#     for right in range(len(nums)):
#         curr_sum += nums[right]
#
#         while curr_sum > k:  # Shrink window if sum exceeds k
#             curr_sum -= nums[left]
#             left += 1
#
#         max_length = max(max_length, right - left + 1)
#
#     return max_length
#
#
# # nums = [3, 1, 2, 5, 1, 1, 2, 1]
# # k = 5
# nums = [2, 3, 1, 2, 4, 3]
# k = 4
#
#
# # find the highest average of k elements in nums
# def flat_sliding(nums, k):
#     max_k_average = 0
#     sum = 0
#
#     for i in range(k):
#         sum += nums[i]
#     max_k_average = sum / k
#
#
#     return max_k_average


def lengthOfLongestSubstring(s: str) -> int:
    letters = ""
    max_length = 0
    left = 0

    for i in range(len(s)):
        letters += s[i]
        print(letters)
        while letters.count(s[i]) > 1:
            print("in", letters)
            letters = letters[1:]
            print("after", letters, left)
            left += 1

        if len(letters) > max_length:
            max_length = len(letters)

    return max_length


print(lengthOfLongestSubstring("bbtablud"))
