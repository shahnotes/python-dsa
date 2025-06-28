def bubble_sort(array):
    for i in range(len(array) -1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            array[j] = key
            j -= 1
    return array

def merge(array1, array2):
    result = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    while i < len(array1):
        result.append(array1[i])
        i += 1
    while j < len(array2):
        result.append(array2[j])
        j += 1
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array

def pivot(array, left, right):
    swap_index = left
    for i in range(left + 1, right + 1):
        if array[i] < array[left]:
            swap_index += 1
            swap(array, swap_index, i)
    swap(array, left, swap_index)
    return swap_index

def quick_sort_helper(array, left, right):
    if left < right:
        pivot_index = pivot(array, left, right)
        quick_sort_helper(array, left, pivot_index - 1)
        quick_sort_helper(array, pivot_index + 1, right)
    return array

def quick_sort(array):
    return quick_sort_helper(array, 0, len(array) - 1)
