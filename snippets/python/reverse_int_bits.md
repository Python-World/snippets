# Reverse bits of an integer
*tags:* **bit manipulation, python**


**Snippet**
```python

def reverseBits(n):
    # Initially all bits are zero
    reverseInt = 0
    # Size of int is 32 bits
    for bitPos in range(32):
        # Check if bit at position "bitPos" is 1,
        # If that bit is 0, then we don't need to add
        # it to reverseInt since it won't make a difference
        if n & (1 << bitPos):
            # Change bit at "bitPos" to 1
            reverseInt = reverseInt | (1 << (31-bitPos))
            
    return revAns

print(reverseBits(10))

```