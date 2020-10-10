# Filter Method
#### The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

_tags_: filter

## Snippet
```
# following code will filter out the even number from a list of numbers

def checkEven(number):
  return number % 2 == 0
  
numberList = [9,2,1,8,6,4,5,3,7]
evenList = filter(checkEven, numberList)

for item in evenList:
  print(item)
```
