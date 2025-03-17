from util import time_it
from time import time
import multiprocessing as mp


@time_it
def recursive_binary_search(nums: list[int], num: int, left: int, right: int):
    if right and left:
        if right < left:
            return -1

        mid = (left + right) // 2
        mid_val = nums[mid]

        if mid_val == num:
            return mid
        if mid_val > num:
            right = mid - 1
        else:
            left = mid + 1
        return recursive_binary_search(nums, num, left, right)


@time_it
def binary_search(nums: list[int], num: int):
    # create two trackers:
    # 1. start index
    # 2. end index
    #
    # Then get the mid index
    #
    # run a while lood for condition ---- left >= right
    # check if the value at mid index is
    # 1. less than the num:
    #   set start to the midIndex +1
    # 2. more than the num:
    #   set end to the midIndex -1
    # 3. equal
    #   return the the index/number

    start_index = 0
    end_index = len(nums) - 1

    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index) // 2
        if nums[mid_index] > num:
            end_index = mid_index - 1
        elif nums[mid_index] < num:
            start_index = mid_index + 1
        else:
            return mid_index


@time_it
def find_multiple_index(nums: list[int], num: int):
    start = 0
    size = len(nums)
    end = size - 1
    while start <= end:
        mid = start + (end - start) // 2
        mid_value = nums[mid]
        if mid_value > num:
            end = mid - 1
        elif mid_value < num:
            start = mid + 1
        else:
            indexes = str(mid)
            left = mid - 1
            while left >= 0 and nums[left] == num:
                indexes = str(left) + "," + indexes
                left -= 1

            right = mid + 1
            while right < size and nums[right] == num:
                indexes += "," + str(right)
                right += 1
            return indexes
    return num


print(find_multiple_index([1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56], 15))

print(binary_search([1, 4, 6, 8, 20, 78, 90, 200], 200))


def find_sorted(start, end, num):
    left = start
    right = end - 1

    while left <= right:
        pos = left + (right - left) // 2
        if pos < num:
            left = pos + 1
        elif pos > num:
            right = pos + 1
        else:
            return pos
    return None


def binary_search(arr, num, start_idx):
    """Performs binary search on a given sub-array"""
    temp = arr
    pos = len(arr) // 2
    while pos:
        if temp[pos] < num:
            temp = temp[pos:]
        elif temp[pos] > num:
            temp = temp[:pos]
        else:
            return start_idx + pos  # Return index in original array
        pos = len(temp) // 2
    return None  # Not found


def parallel_find_sorted(arr: list[int], num):
    """Uses multiprocessing to speed up the binary search"""
    num_cores = mp.cpu_count() - 1
    chunk_size = len(arr) // num_cores
    chunks = [
        (arr[i * chunk_size : (i + 1) * chunk_size], num, i * chunk_size)
        for i in range(num_cores)
    ]

    with mp.Pool(processes=num_cores) as pool:
        results = pool.starmap(binary_search, chunks)

    # Remove None values and return the found index
    found = [res for res in results if res is not None]
    return found[0] if found else "Not found"


if __name__ == "__main__":
    start = 1
    end = 10_000_000_000_000
    num = 9  # Number to find

    t1 = time()
    print(find_sorted(start, end, num))
    print("time taken: ", time() - t1)
