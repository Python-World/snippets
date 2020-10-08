# Show use of list comprehension 
*tags:* **list, list comprehension**


**Snippet**
```python


num_list = [2,3,6,7,8,9,0]

def pow_base_two(num):
 return pow(num,2)

#Solution with list comprehension

num_result_pow = [pow_base_two(num) for num in num_list ]

print(num_result_pow)


```


```python


num_list = [2,3,6,7,8,9,0]

def pow_base_two(num):
 return pow(num,2)

#Solution without list comprehension

num_result_pow = []

for num in num_list:
    num_result_pow.append(pow_base_two(num))

print(num_result_pow)

```