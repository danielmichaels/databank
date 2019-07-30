#!/usr/bin/env python3

"""Decorator example script."""

# these are closures
print('Closure recap')


def outer_function():
    """Hardcoded the msg"""
    msg = 'hi'

    def inner_function():
        print(msg)

    # return inner_function() # will execute the function.
    return inner_function  # returns it ready to be executed, but not executed.


outer_function()  # will return the msg if inner_function has been executed,
# if not, will return nothing.
execute_inner = outer_function()  # now the execute_inner will execute it.
execute_inner()  # now the inner_function will print msg.


def outer_function2(msg):
    """Set msg as a arg"""

    # message = msg # now remove this and directly put it in the inner_func.
    def inner_function():
        # print(message) # orginally took in the message in outer_func.
        print(msg)

    # return inner_function() # will execute the function.
    return inner_function  # returns it ready to be executed, but not executed.


hi_func = outer_function2('hi!')
bye_func = outer_function2('bye!')

hi_func()
bye_func()
print('End Closure recap\n')

# end closures.

# start decorators

"""                     What is a decorator?

A function that takes in another function as an argument, adds some new 
functionality and returns a new function whilst not altering the original 
functions source code.
"""


def decorator_function(orginial_function):
    def wrapper_function():
        print('I ran before {}'.format(orginial_function.__name__))
        return orginial_function()

    return wrapper_function


@decorator_function  # == display = decorator_function(display)
def display():
    print('display function ran!')


print('normal closure below')
decorator_function(display())  # normal closure.
print('\nthe literal decorator is being called..')
without_brackets = decorator_function(display)  # this is a decorator, w/out @.
without_brackets()
print('\n.. now for the decorator!')
display()  # calling the @decorator_function, decorator.

"""Now for decorators that take arguments:
Using *args and **kwargs can be the solution to this"""


def postional_args(fn):
    def wrapper(*args, **kwargs):  # wrapper takes the *args, **kwargs
        print()
        print('Now with added args!')
        return fn(*args, **kwargs)  # and returns them in the fn function.

    return wrapper


@postional_args
def fullname(first, last):
    print('My full name is {} {}'.format(first, last))


fullname('Tony', 'Stark')


class DecoratorClass(object):
    """Classes can be used as decorators too!"""

    def __init__(self, function_to_decorate):
        self.function_to_decorate = function_to_decorate

    def __call__(self, *args, **kwargs):
        """__call__ behaves like the 'wrapper_function'"""
        print()
        print('Now with added class!!')
        print(f'Decorated Function: {self.function_to_decorate.__name__}')
        return self.function_to_decorate(*args, **kwargs)


@DecoratorClass
def test_class():
    print('Class decorator is working!')


@DecoratorClass
def much_args(letter, word, num):
    print(f'{letter} - {word} - {int(num)}')


test_class()
much_args('L', 'Dog', '15')

"""Specific use cases; real world examples

Functools wraps in a nutshell takes a function used in a decorator and 
adds the functionality of copying over the function name, docstring, arguments 
list, etc. It is also a decorator!

"""
from functools import wraps


def logger(function_to_log):
    import logging
    logging.basicConfig(filename='{}.log'.format(function_to_log.__name__),
                        level=logging.INFO)

    @wraps(function_to_log)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {} and  kwargs: {}'.format(args, kwargs)
        )
        return function_to_log(*args, **kwargs)

    return wrapper


def timer(func_to_time):
    import time

    @wraps(func_to_time)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func_to_time(*args, **kwargs)
        t2 = time.time() - t1
        print('ran {} in {} secs'.format(func_to_time.__name__, t2))
        return result

    return wrapper


# @timer # this will take in wrapper as its argument unless functools used.
@timer  # now that functools is added, it will evaluate as expected.
@logger
@timer
def display_stuff(name, age, weight):
    print()
    print(f'{name} is {age} years old and weighs {weight} kilograms')


display_stuff('Donatello', '50', '123')

# display1 = logger(timer(display)) # this is how chained decorators look.
# display1()
