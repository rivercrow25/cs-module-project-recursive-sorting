# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # base case
    if end >= start:
        # get the middle ground
        mid = (start + end) // 2
        # check if the middle is the target
        if arr[mid] == target:
            return mid
        # check if target is less then middle
        elif arr[mid] > target:
            # run the function again moving end to 1 before mid
            return binary_search(arr, target, start, mid-1)
        # check if target is greater
        else:
            # run the function again moving end to 1 after mid
            return binary_search(arr, target, mid + 1, end)
    else:
        # if there are no elements in the array return none
        return -1
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    pass
    # Your code here
