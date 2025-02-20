def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        mid_val = arr[mid]

        if mid_val == target:  # Target found
            return mid
        elif mid_val < target:  # Narrow the search to the right half
            low = mid + 1
        else:  # Narrow the search to the left half
            high = mid - 1

    return -1


arr = [4, 6, 3, 2, 5, 7, 1]

binary_search(arr, 3)
