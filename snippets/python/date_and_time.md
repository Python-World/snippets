# Check Current Date and Time

*tags:* python, datetime

`datetime`: The datetime module supplies classes for manipulating dates and times.

### Snippet 
```
import datetime 

# now() method returns current datetime object
cur_time = datetime.datetime.now()  

print("Date: ", cur_time.day, "/", cur_time.month, "/", cur_time.year)
print("Time: ", cur_time.hour, "h:", cur_time.minute, "m:", cur_time.second, "s")
```
