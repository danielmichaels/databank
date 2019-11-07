"""All the things I wish someone helped me with when I started out."""

import time

# This is how we import "modules", what's a module?
# A module at its simplest, is another script - what you are reading, is a script.
# when we import 'time' we are saying 'let me access everything in that script'
# this lets us 'call' or use any function or method within that script - with a caveat.

string = "This is a string"
string2 = "single quotes, or double quotes, you decide!"
string3 = "strings can contain anyhing really; 1, True [] {} ()"

integer = 1  # I am a number
float_ = 3.14159  # A decimal point number
bool1 = True
bool2 = False  # binary, 0 or 1, true or false!

# Variables

my_name = "Dan"
my_number = 21
do_i_believe_in_you = True
satoshi = 0.00000001

# we can do stuff to variables
satoshi_plus_number = my_number + satoshi
print(satoshi_plus_number)
print(my_name, "jersey number is", my_number)
octet = 2 ** 8
print("How many hosts in one octet?", octet)
print("um, that not true if its zero indexed is it?", octet - 1, "now we talking!!")

# List all the things!!
# lists can contain things; variables, strings, other lists, dictionaries, tuples, etc

cats = ["skittles", "moggy", "snowball", "mojo"]
random_stuff = [
    "toothpick",
    8,
    5.5,
    True,
    ["a", "list", "within", "a", "list"],
    my_name,
    satoshi_plus_number,
]
print(random_stuff)
# lists are cool, but how does one get something from a list? well,
# lists are indexed by number starting a zero.

# what's the coolest cats name?
print(cats[0])  # the first item, starts at Zero.
# there is how many bits in a byte?
print("there is", random_stuff[1], "bits in a byte!")
# I forgot my name... which is second last.
print(random_stuff[-2])
# lets get the word list from the list with the list named 'random_stuff'
print(random_stuff[4][1])
# we got the list at the fourth index, then got the word 'list' at the first index of that list! think on that...

# can I just find something in a list, even though I don't know its index position?
print("skittles" in cats)  # this will return a Boolean (true/false)
print("santa's little helper" in cats)  # False! not in that list

# what a segue into flow control!
# loops, if/elif/else
# for loops
for cat in cats:
    print(cat)
    # prints ['skittles', 'moggy', 'snowball', 'mojo']
# cat means NOTHING, cats does, that references the list name cats! lets see that again!

print()  # here just to separate the outputs
for sex_in_the_city_is_on_tv in cats:
    print(sex_in_the_city_is_on_tv)
    # if the list 'cats' didn't exist we would get an Error and this script would fail.

print()  # here just to separate the outputs
for items in random_stuff:
    print("thing in list:", items)

print()  # here just to separate the outputs

if "skittles" in cats:
    print("she sits on me!")
else:
    print("no more sitting on me!")
# why didn't the 'else' print? flow control

if "tiger" in cats:
    print("she sits on me!")
else:
    print("no more sitting on me!")
# whats the difference here? if statements or flow control statements will check
# in this case, the list and output what it finds first, execute that and then quit.

# what if we wanted to return a result for each item in a list? Then we need a for!
print()  # here just to separate the outputs
for each_item_in_the_list in cats:
    if "skittles" in each_item_in_the_list:
        print("YAY, shes here!")
    else:
        print(each_item_in_the_list, "is not skittles!!")
# for every item in that list that does not equal 'skittles' we print something
# if the item has 'skittles' in it, we print something.

print()  # here just to separate the outputs

for number in range(7):
    if number > 4:
        print("if statement executed on", number)
    elif number < 3:
        print("elif statement executed on", number)
    else:
        print("else executed on", number)
# flow control here again, look it over and think about it. Why does this work
# the way it does?

# Yo dawg, I heard you like functions so I put a function in ya function and turned it into a decorator!

# functions take inputs, do something to them and return an output (generally)
# they are repeatable and save us from writing the same things over and over again!


def multiply(thing1, thing2):
    """must be an integer"""
    thing1 = thing1 * 3
    thing1_plus_thing2 = thing1 + thing2
    return thing1_plus_thing2


# because we have defined a function and given it parameters (things1 & 2)
# we must 'call' it with those parameters. Like so,

multiply(50, 3)  # this will not print anything..
print(multiply(50, 3))  # so I put it inside a.. print.. function!


def multiply_if_int(a, b):
    """If the parameters are not integer's add them together, else multiply"""
    if a or b == type(int):  # == checks the value
        return a + b
    else:
        return a * b


print(multiply_if_int(1, 2))
print(multiply_if_int("1", "2"))
# think about how this works

# if you don't recall what 'type' is..
print(
    f"""
here is a reminder of type in python:
type(int) == {type(my_number)}
type(float) == {type(float_)}
type(cats) == {type(cats)}
type(my_name) == {type(my_name)}
"""
)

# dict's! big dicts, little dicts, dicts of all shapes and sizes!!
# above I said, a list is index by number (starting at.. zero)
# dictionaries, are like lists, except they are accessed by a 'key'. And,
# each key points a value. Keys are unique, their values are not. This makes dict
# lookups very fast.
# dicts are 'key':'value' stores and are defined like so,

dog = {"breed": "lab", "age": 5, "colour": "black", "favourite toy": "tennis ball"}
print(dog)
# now dict's are very powerful, so this is a overview rather than a detailed exploration.
# if you want to list all the keys try this:
print(list(dog))
# or
print(dog.keys())
# or
for key in dog.keys():
    print(key)

# if we want the values..
print()
print(dog.values())
print()
for value in dog.values():
    print(value)

# how about both?
print(dog.items())
print()
# we call items()
for key, value in dog.items():
    print(key, ":", value)
# try calling just key or value in dog.items(), what happens? why?

# last thing... import time, lets see that in action
print()
print("comment out time.sleep(1) if this gets annoying")
print("or hit CTRL-C")
for x in range(5):
    print("one second elapsed")
    time.sleep(1)
    # sleep is a function within the module (script) time and it takes
    # a parameter, which in this case is an integer which represents
    # a 1 second.


# I think thats enough for now.
