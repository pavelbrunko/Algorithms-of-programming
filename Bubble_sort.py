# Import randint for creating a random array
from random import randint

# Defining a function
def bubble_sort(nums):
    # First cycle for passing through the entire array
    for i in range(len(nums)-1):
        # Second cycle for checking the unsorted part of the array
        for j in range(len(nums)-i-1):
            # Condition if left gidit greater than right digit
            if nums[j] > nums[j+1]:
                # Swapping digits, if the condition was done
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
# Creating a list for our random array
nums = []
for i in range(10):
    nums.append(randint(1, 99))
# Print the results
print(nums)
bubble_sort(nums)
print(nums)