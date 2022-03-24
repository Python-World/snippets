# find n largest/smallest number

## heapq
`heapq` provides an implementation of the heap queue algorithm. This module provides two useful functions: `heapq.nlargest` and `heapq.nsmallest`. 
These functions return the specified number of largest/smallest elements from a Python iterable like a list, tuple and others.

## snippet
```
# Example Python program that finds the largest/smallest n elements

import heapq
target = [8, 0, 6, 1, 3, 9, 7, 5, 4]

findCount = 3

largests = heapq.nlargest(findCount, target)
smallests = heapq.nsmallest(findCount, target)
print(f'{findCount} largest nums: {largests}')
print(f'{findCount} smallest nums: {smallests}')
```
