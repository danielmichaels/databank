# Python

Storage for notes, snippets and more

## dict() v {}

- `{}` is a literal for a dictionary object
- `dict()` is a function that creates dictionary *objects* 
- Using `{}` is faster than `dict()`
- When to use each:
  - `{}`:
    - Best used for speed,
    - When you are displaying the contents in the source code
  - `dict()`:
    - Explicitly determining `dict()` usage over `{}` as a set,
    - Need to convert a type,

### Example

```python

from dis import dis

def a():
  a = {}
  b = dict()
  
dis(a)

#                        output
>>>
>>>  2           0 BUILD_MAP                0
>>>              2 STORE_FAST               0 (a)
>>>
>>>  3           4 LOAD_GLOBAL              0 (dict)
>>>              6 CALL_FUNCTION            0
>>>              8 STORE_FAST               1 (b)
>>>             10 LOAD_CONST               0 (None)
>>>             12 RETURN_VALUE
```

