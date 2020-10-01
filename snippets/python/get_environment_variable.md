# Get a Specific Environment Variable
*tags:* **os, python**

`os` is a built-in python module to interact with the operating system.

**Snippet**
```python
import os

# This is the environment variable that would be fetched.
# For example here we are getting the 'Path' environment
# variable
env_var = 'Path' 

# fetched_result variable holds the value
# which was to be retrieved
fetched_result = os.environ[env_var]

```