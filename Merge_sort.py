# Import some necessary libs for creating an array and for partition
import random 
from random import randint

# Creating an array
nums = []
for i in range(10):
    nums.append(randint(1, 99))
print(nums)

# Define merge sort function
def merge_sort(nums):
    # Check if array is greater than 1
    if len(nums) > 1:
        # Divide array on two parts
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        # Call recursively merge sort function
        merge_sort(left)
        merge_sort(right)

        # Define indexes for left, right and initial arrays
        l = r = p = 0

        # Merge sorted subarrays
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                nums[p] = left[l]
                l += 1
            else:
                nums[p] = right[r]
                r += 1
            p += 1
        
        # Add all right part if left already added in it's entirety
        while r < len(right):
            nums[p] = right[r]
            r += 1
            p += 1

        # Do the same for the left part
        while l < len(left):
            nums[p] = left[l]
            l += 1
            p += 1
    # Return sorted array
    return nums

print(merge_sort(nums))


