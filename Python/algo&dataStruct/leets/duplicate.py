from typing import List

#
# def is_duplicate(nums: List[int]) -> bool:
#     if len(nums) > len(set(nums)):
#         return True
#
#     return False
#
#
# print(is_duplicate([1, 2, 3, 4, 5, 5]))


# def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
#     hashSet: dict[str, int] = {}
#     for i in range(0, len(nums)):
#         if str(nums[i]) in hashSet and i - hashSet[str(nums[i])] <= k:
#             return True
#         else:
#             hashSet[str(nums[i])] = i
#     return False
#
#
# print(containsNearbyDuplicate([1, 5, 3, 4, 2, 5], 1))


def containsNearbyAlmostDuplicate(
    nums: List[int], indexDiff: int, valueDiff: int
) -> bool:
    hashSet: dict[str, int] = {}
    for i in range(0, len(nums)):
        if (
            str(nums[i]) in hashSet
            and i - hashSet[str(nums[i])] <= indexDiff
            and abs(nums[i] - nums[hashSet[str(nums[i])]]) <= valueDiff
        ):
            return True
        else:
            hashSet[str(nums[i])] = i
    return False


print(4 - 6)
print(abs(4 - 6))
print(containsNearbyAlmostDuplicate([8, 7, 15, 1, 6, 1, 9, 15], 1, 3))


# write a function to accep arrays of string and return longest string
def get_longest_string(arr: List[str]):
    return arr
