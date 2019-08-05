# Python Snippets

## `dict()` v `{}`

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

## Get System Info

`psutil` package

```python
import psutil

battery = psutil.sensors_battery()
print(battery)
print(battery.percent)
```

## __repr__


- Good for exploratory programming, doctests, documentation, and debugging
- Best practice, should return string syntax which another programmer could use to instantiate that class - `eval(repr(x)) == x`
- If not viable, use the default object `<ClassToBeRepr ...>` with some extra information tacked on.
- allows `repr(cls)` to be used

```python

class Coordinate:
    # at a minimum all classes should have a single docstring over a pass
    '''Coordinate on Earth'''
        
    def __repr__(self):
        return f'Coordinate({self.lat}, {self.long})'   

>> cle.__repr__() # returns 'Coordinate(x,x)'
>> repr(cle) # returns 'Coordinate(x,x)'
# which could be used to create another instance of the class
```


