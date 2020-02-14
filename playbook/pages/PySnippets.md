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
* [Requests XHR](#requests-xhr)

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

## Selenium setup

Simple driver setup

```python
def setup_driver():
    """Setup the driver"""
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", os.getcwd())
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                           "application/csv")

    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(firefox_profile=profile, options=options)
    driver.implicitly_wait(30)
    return driver
```

## iPython 6.5 Vim Keybindings

**Taken from [SO](https://stackoverflow.com/questions/38443907/how-does-one-set-specific-vim-bindings-in-ipython-5-0-0/38810821#38810821) user [jellycola](https://stackoverflow.com/users/2340015/jellycola)**


According to the IPython docs, you can specify Keyboard Shortcuts in a startup configuration script.

Instead of rebinding jk to ESC, I'm making a unicode "j" (u'j') followed by a unicode "k" (u'k') inside of VimInsertMode() a shortcut for a prompt_toolkit event that switches to navigation mode.

I created a `.ipython/profile_default/startup/keybindings.py` with the following code:

```python
from IPython import get_ipython
from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.filters import HasFocus, ViInsertMode
from prompt_toolkit.key_binding.vi_state import InputMode


ip = get_ipython()

def switch_to_navigation_mode(event):
    vi_state = event.cli.vi_state
    vi_state.input_mode = InputMode.NAVIGATION

if getattr(ip, 'pt_app', None):
    registry = ip.pt_app.key_bindings
    registry.add_binding(u'j',u'k',
                         filter=(HasFocus(DEFAULT_BUFFER)
                                 & ViInsertMode()))(switch_to_navigation_mode)

```

## Guard Clause Type Safety

How to check if variable is expected type.

```python
if type(var) not in (int, float):
  raise TypeError(f'{var} must be a number')
```

## Requests XHR

The easiest way to replay an XHR in python is to go into your browsers network tab,
identify the request and right click selecting _copy as cURL_.

Open Postman and click on _import_ in the top left. On the right is _paste raw text_, paste in
the cURL command and hit import. Then in the main body, on the right hand side is
a link to _Code_. Selecting this will generate a massive selection of code formatted
output for that command. Select python and run it in your script!
