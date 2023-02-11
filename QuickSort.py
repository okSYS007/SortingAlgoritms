
from time import perf_counter
import random

def partition(nums, low, high):
     
    # choose the rightmost element as pivot
    pivot = nums[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if nums[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (nums[i], nums[j]) = (nums[j], nums[i])
 
    # Swap the pivot element with the greater element specified by i
    (nums[i + 1], nums[high]) = (nums[high], nums[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 

def quicksort(nums, low, high):

    if low < high:
     
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(nums, low, high)
 
        # Recursive call on the left of pivot
        quicksort(nums, low, pi - 1)
 
        # Recursive call on the right of pivot
        quicksort(nums, pi + 1, high)

    return nums



nums = random.sample(range(0, 1000), 1000)
#nums = [4, 2, 2, 8, 3, 3, 1]
size = len(nums)

start = perf_counter()
print(quicksort(nums, 0, size - 1))
print(f"time: {(perf_counter() - start):.02f}")

