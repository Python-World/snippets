# Basic File Handling


## Writing

Open file in current directory to overwrite file contents. Creates file if it doesn't exist.
```
file = open("file.txt", "w")
file.write("hello earth!")
```
File contents:
```
hello earth!
```
## Reading

Open file for read only. Read entire contents of file.
```
file = open("file.txt", "r")
file_contents = file.read()
```
Reads:
```
hello earth!
```

## Appending

Open file for appending. This means the existing file content is kept.
```
file = open("file.txt", "a")
file.write("\nhello universe!") # note:"\n" writes a newline 
```
File contents:
```
hello earth!
hello universe!
```
## Read file line by line

Make a list holding each line in the file
```
file = open("file.txt", "r")
lines_in_file = file.readlines()

for each_line in lines_in_file:
    print(each_line)
```
prints:
```
hello earth!
hello universe!
```

## Check if file exists 

```
from pathlib import Path

file_to_find = Path("file.txt")

if file_to_find.exists():
    print("file exists") 
else:
    print("file not found") 
```

## Delete file

```
from pathlib import Path

file_to_delete = Path("file.txt")
file_to_delete.unlink()
```
