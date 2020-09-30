---
title: run time python version
tags: sys,python
---

Fetch runtime python version
- `sys` built in module help you to find more information

```python
import sys
version = sys.version_info
print(f'{version.major}.{version.minor}.{version.micro}')

# 3.8.3
```