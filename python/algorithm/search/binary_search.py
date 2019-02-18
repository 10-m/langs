#!env python3
# -*- coding: utf-8 -*-

def binary_search_iterator(sorted_list, target):
    left_pointer = 0
    right_pointer = len(sorted_list)
    while left_pointer < right_pointer:
        mid_idx = (right_pointer - left_pointer) // 2 + left_pointer
        mid_val = sorted_list[mid_idx]
        if mid_val == target:
            return mid_idx
        if target < mid_val:
            right_pointer = mid_idx
        if target > mid_val:
            left_pointer = mid_idx + 1
    return "Value not in list"

def binary_search_recursive(sorted_list, target):
    if not sorted_list:
        return 'value not found'

    mid_idx = len(sorted_list)//2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
        return mid_idx
    elif mid_val > target:
        left_half = sorted_list[0:mid_idx]
        return binary_search_recursive(left_half, target)
    else:
        right_half = sorted_list[mid_idx+1:]
        result = binary_search_recursive(right_half, target)
        if result == "value not found":
            return result
        else:
            return result + mid_idx + 1

# test cases
print(binary_search_iterator([5,6,7,8,9], 9))
print(binary_search_iterator([5,6,7,8,9], 10))
print(binary_search_iterator([5,6,7,8,9], 8))
print(binary_search_iterator([5,6,7,8,9], 4))
print(binary_search_iterator([5,6,7,8,9], 6))

print(binary_search_recursive([5,6,7,8,9], 9))
print(binary_search_recursive([5,6,7,8,9], 10))
print(binary_search_recursive([5,6,7,8,9], 8))
print(binary_search_recursive([5,6,7,8,9], 4))
print(binary_search_recursive([5,6,7,8,9], 6))
