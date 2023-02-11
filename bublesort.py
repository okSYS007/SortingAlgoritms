
from time import perf_counter
import random

def bublesort(nums):
    n = len(nums)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums
 

nums = random.sample(range(0, 1000), 1000)

start = perf_counter()
print(bublesort(nums))
print(f"time: {(perf_counter() - start):.02f}")

