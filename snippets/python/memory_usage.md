# Memory Usage
The memory used by an object inside a code can be checked by sys.getsizeof()

*tags:* python, memory, objects

### Syntax:
```
sys.getsizeof(object_name))
```

### Snippet:
```
import sys

num = 21

print(sys.getsizeof(num))

# In Python 2, 24
# In Python 3, 28
```
