# Flatten 2D List

*tags:* python

```
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# output: [1,2,3,4,5,6,7,8,9]

l = []
def flatten_array(matrix):
    return ",".join(flat(matrix, 0, 0))

def flat(matrix, row, col):
    l.append(str(matrix[row][col]))
    if col == len(matrix[row]) - 1:
        if row == len(matrix) - 1:
            return l
        return flat(matrix, row + 1, 0)
    return flat(matrix, row, col + 1)


print("Enter number of rows: ", end="")
matrix_rows = int(input().strip())
print("Enter number of columns: ", end="")
matrix_columns = int(input().strip())

matrix = []
print("Enter matrix elements:")
for _ in range(matrix_rows):
    matrix.append(list(map(int, input().rstrip().split())))
print("Entered matrix is: ", matrix)

result = flatten_array(matrix)
print("Resultant list: [", end="")
print(result, end="]")
```
