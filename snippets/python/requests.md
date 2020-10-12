# Make a HTTP request

*tags:* python, requests

`requests`: The datetime module supplies classes for manipulating dates and times.
 The requests module allows you to send HTTP/1.1 requests and parse a response

### Snippet
```
import requests

name = str(input())
req = requests.get("https://github.com/" + name)
response = req.status_code
if response == 404:
    print("This does not exist")
else:
    print("This exists")
```
