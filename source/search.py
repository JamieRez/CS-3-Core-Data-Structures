#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array) - 1:
        return None
    else:
        if array[index] == item:
            return index
        else:
            return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array)
    while(not right - 1 == left):
        if item == array[left]:
            return left
        elif item == array[right - 1]:
            return right - 1
        midIndex = (right + left) // 2
        if item < array[midIndex]:
            right = midIndex
        elif item > array[midIndex]:
            left = midIndex
        else:
            return midIndex
    return None


def binary_search_recursive(array, item, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(array)
    if left == right - 1:
        return None
    if array[left] == item:
        return left
    elif array[right - 1] == item:
        return right - 1
    midIndex = (right + left) // 2
    if item < array[midIndex]:
        return binary_search_recursive(array, item, left, midIndex)
    elif item > array[midIndex]:
        return binary_search_recursive(array, item, midIndex, right)
    else:
        return midIndex
