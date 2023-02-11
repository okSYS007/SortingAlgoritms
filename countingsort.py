
from time import perf_counter
import random

def bublesort(nums):

    size = len(nums)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[nums[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        nums[i] = output[i]

    return nums

#nums = random.sample(range(0, 1000), 1000)
nums = [4, 2, 2, 8, 3, 3, 1]
start = perf_counter()
print(bublesort(nums))
print(f"time: {(perf_counter() - start):.02f}")

