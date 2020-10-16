# Reduce Method
### The reduce() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.

_tags_: reduce

# Snippet
```
# following code will reduce a list to give a result based on particular function

from functools import reduce

list_of_numbers = [1, 2, 3, 4, 5]
prod = 1

def multiplication(a, b):
	return a*b

result = reduce(multiplication, list_of_numbers)
print(result)
```
