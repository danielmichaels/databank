# Python Snippets



<!-- vim-markdown-toc GFM -->

* [pip upgrade all packages](#pip-upgrade-all-packages)
* [`dict()` v `{}`](#dict-v-)
  - [Example](#example)
* [Get System Info](#get-system-info)
* [__repr__](#repr)
* [Dict Comprehensions](#dict-comprehensions)
* [URL decode](#url-decode)
* [Deleted Pip?](#deleted-pip)

<!-- vim-markdown-toc -->
## pip upgrade all packages

```python
import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
```

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

## Dict Comprehensions

Syntax `{ k:v for (k,v) in iterable}` or `{k:v for (k,v) in dict.items()}`

Examples:

1. get base 2 numbers from given list of numbers:
  1. `{number: 2**number for number in [1,2,3,4,5,6,7,8]}`
2. get `ord`(unicode representation) of each char in string or list:
  1. `{letter: ord(letter) for letter in 'string'}`
3. convert Fahrenheit to Celsius:
  1. `{k:(float(5)/8)*9(v-32) for (k,v) in dict({'t1':0, 't2':30}}).items()`
4. conditionals:
  1. `{k:('even' if v%2==0 else 'odd') for (k,v) in dict({'a':1,'b':2,'c':3,'d':4}).items()}`
  2. `{number: ('even' if number%2==0 else 'odd') for number in [1,2,3,4,5]}`

## URL decode

For quickly decoding url or individual encodings.

```
from urllib.parse import unquote

# URL example
url = 'example.com?title=%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D0%B0'
unquote(url)
>> 'example.com?title=правовая+защита'

# Single char example
unquote('%3b')
>> ;
```

## Deleted Pip?

Arch Linux pip issues happen. If `pip` gets badly broken try this:

```sh
trizen -Rns python-pip
curl https://bootstrap.pypa.io/get-pip.py | sudo python
``


