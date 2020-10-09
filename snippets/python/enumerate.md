# Enumerate in Python

*tags:* python, enumerate

* `enumerate`: This function iterates through an interable object like a string or list and returns an enumerate object with associated counter starting from zero by default.

### Syntax:
```
enumerate(iter_object, counter = 0)
```

## Snippet:

```
# Iterable string object
it_string = "hacktober"
# Iterable list object
it_list = ['h', 'a', 'c', 'k']

print(list(enumerate(it_string)))

# count parameter with a value of 5
for val, count in enumerate(it_list, 5):
    print(count, val)
```
