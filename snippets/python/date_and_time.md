# Check Current Date and Time

*tags:* python, datetime

`datetime`: The datetime module supplies classes for manipulating dates and times.

### Snippet 
```
import datetime 

# now() method returns current datetime object
cur_time = datetime.datetime.now()  

print("Date today:",f"{cur_time:%Y-%m-%d}")
print("Time:", f"{cur_time:%H:%M:%S%z}")
```
