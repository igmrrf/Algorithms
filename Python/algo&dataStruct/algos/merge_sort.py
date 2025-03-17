from util import time_it


def merge_sorted(a, b, arr, key, descending):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if descending:
            if a[i][key] >= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
        else:
            if a[i][key] <= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


def merge(arr, key: str, descending: bool):
    if len(arr) <= 1:
        return

    pos = len(arr) // 2

    # sorted_list = True
    # for i in range(1, size):
    #     if arr[i] < arr[i - 1]:
    #         sorted_list = False
    #         break
    #
    # if sorted_list:
    #     print("ARR,", arr)
    #     return arr
    #
    # else:
    left = arr[pos:]
    right = arr[:pos]

    merge(left, key, descending)
    merge(right, key, descending)
    merge_sorted(left, right, arr, key, descending)


def merge_sort(nums1, nums2):
    sorted = []
    len_l = len(nums1)
    len_r = len(nums2)
    left, right = 0, 0
    times = 0
    while left < len_l or right < len_r:
        if right >= len_r:
            sorted = sorted + nums1[left:]
            break
        elif left >= len_l:
            sorted = sorted + nums2[right:]
            break

        if nums1[left] <= nums2[right]:
            sorted.append(nums1[left])
            left += 1
        else:
            sorted.append(nums2[right])
            right += 1

    print(times)
    return sorted


nums1 = [1, 3, 10, 38, 48, 58]

# nums2 = [8, 14, 8, 3]
#
elements = [
    {"name": "vedanth", "age": 17, "time_hours": 1},
    {"name": "rajab", "age": 12, "time_hours": 3},
    {"name": "vignesh", "age": 21, "time_hours": 2.5},
    {"name": "chinmay", "age": 24, "time_hours": 1.5},
]

nums2 = [8, 14, 2, 9, 4, 19, 5, 3, 6, 33, 7]


merge(elements, "name", descending=True)

print(elements)
