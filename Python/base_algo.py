from util import time_it, swap


def shell_sort(arr):

    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                if arr[j - gap] > anchor:
                    arr[j] = arr[j - gap]
                    j -= gap

            arr[j] = anchor
        gap = gap // 2


nums2 = [8, 14, 2, 9, 4, 19, 5, 3, 6, 33, 7]


shell_sort(nums2)
print(nums2)
