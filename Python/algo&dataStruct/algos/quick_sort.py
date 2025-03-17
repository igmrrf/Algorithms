from util import time_it
import random


def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def inner_lomuto_quick_sort(elements, start, end):
    if start < end:
        pi = lomuto_partition(elements, start, end)
        inner_lomuto_quick_sort(elements, start, pi - 1)
        inner_lomuto_quick_sort(elements, pi + 1, end)


def lomuto_quick_sort(elements):
    inner_lomuto_quick_sort(elements, 0, len(elements) - 1)


def lomuto_partition(elements, start, end):
    pivot = elements[end]  # Pivot is the last element
    i = start - 1  # Place for the smaller element

    for j in range(start, end):
        # If the current element is smaller than or equal to the pivot
        if elements[j] <= pivot:
            i += 1
            swap(i, j, elements)

    # Place pivot in its correct position
    swap(i + 1, end, elements)
    return i + 1  # Return pivot index


# Hoare partitioning
def hoare_partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    size = len(elements)
    while start < end:
        while start < size and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end


def inner_quick_sort(elements, start, end):
    if start < end:
        pi = hoare_partition(elements, start, end)
        inner_quick_sort(elements, start, pi - 1)
        inner_quick_sort(elements, pi + 1, end)


# Hoare partitioning
def quick_sort(elements):
    inner_quick_sort(elements, 0, len(elements) - 1)


nums1 = [4, 10, 29, 5, 2, 8]


def lomuto_quick_sorting(elements, start, end):
    pivot = elements[end]
    i = start - 1

    for j in range(start, end):
        if elements[j] > pivot:
            i += 1
            swap(i, j, elements)
    swap(i + 1, end, elements)
    return i + 1


nums2 = []
# for i in range(10):
#     num = random.randint(1, 10000)
#     nums1.append(num)
#     nums2.append(num)


@time_it
def run():
    # quick_sort(nums1)
    lomuto_quick_sort(nums1)


run()
