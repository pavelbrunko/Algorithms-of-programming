# Import some necessary libs for creating an array and for partition
import random 
from random import randint

# Creating an array
alist = []
for i in range(10):
    alist.append(randint(1, 99))
print(alist)

# Define the recursive quick_sort function  
def quick_sort(alist, start, end):
    # Condition for len of array be greater than 1
    if end - start > 1:
        # Calling a partition function for getting an index of support element p
        p = partition(alist, start, end)
        # Calling quick_sort function for the left part
        quick_sort(alist, start, p)
        # Calling quick_sort function for the right part
        quick_sort(alist, p + 1, end)

# Define the partition funtion 
def partition(alist, start, end):
    # Choose the supprting element which is equal to the first element in this part of array
    pivot = alist[start]
    # Defining the step from the diffent ends of our array 
    i = start + 1
    j = end - 1

    # Using while cycle we can step from index to index and check if the digits in the left part are less than pivot and 
    # if the digits in the right part are greater than pivot
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        # If i <= j we continue to go through the array
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        # Else we swapping pivot and alist[i] elements
        else:
            alist[start], alist[j] = alist[j], alist[start]
            # Retuning the j and the element alist[j] become a new support element
            return j

# Calling the quick_sort function and printing the result
quick_sort(alist, 0, len(alist))
print(alist)