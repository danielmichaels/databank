#!/usr/bin/env python3

"""This is a basic class tutorial script taken almost verbatim from the
    excellent video from Corey Schafer's youtube channel.

Property Decorators:

property() is a built-in function that creates and returns a property object.

property(fget=None, fset=None, fdel=None, fdoc=None) #default kwargs

thereby we could call the property by using the keywords, as well as setting
the syntactic sugar of @property.getter for instance.

see: https://www.programiz.com/python-programming/property
"""


class Employee:
    """Base class for Employee object."""

    raise_percentage = 1.04  # Class Attribute:

    # meaning it is accessible across the entire class - can be overwritten.

    def __init__(self, first, last, pay, hours_worked):
        self.first = first
        self.last = last
        # self.email = first + last + '@email.com' # not needed as now method.
        self.pay = pay
        self.hours_worked = hours_worked

    @property
    def email(self):
        """Example of @property.

        Allows the method to be called as an attribute.
        """
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        """Example of the power of setter property."""
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        """Example of deleter property."""
        print(f'{self.fullname} deleted!!')
        self.first = None
        self.last = None

    def apply_raise(self):
        # makes the raise_percentage accessible.
        self.pay = int(self.pay * self.raise_percentage)

    def __repr__(self):
        # used as a 'developer' tool.
        return 'Employee: {} {}, ${}p.a. , {}'.format(
            self.first, self.last, self.pay, self.email)

    def __str__(self):
        # used as a 'client' tool. Overrides __repr__.
        return 'this is the __str__ representation'


class Developer(Employee):
    """Developer class."""

    _langs = [
        'Python', 'Java', 'COBOL', 'Elixir'
    ]

    def __init__(self, first, last, pay, hours_worked, language='Python'):
        super().__init__(first, last, pay, hours_worked)
        # super allows MRO to change dynamically with parent. Delegates method
        # calls to parent/ sibling type. By not naming parent explicitly code
        # is more maintainable.
        self.language = language


    @classmethod
    def langs(cls):
        """Example of a ClassMethod - it does not need to instantiated
        and can call Class Attributes such as the _langs list.

        This can cause issues if for instance, you want to add to the _langs
        list via

        dev = Developer._langs = [ 'JavaScript', 'Erlang' ]

        when calling dev.langs() it will return the original list, rather than
        the updated one. Why? Because @classmethod will call the class not
        the instance. Meaning, it will not return the newly instantiated list
        but the class attribute.

        In this example, if the _langs needed updating dynamically then just
        call the method, and it will work as expected.
        """
        return cls._langs


class Executive(Employee):
    """Executive class."""

    bonus = 1.07

    def __init__(self, first, last, pay, hours_worked):
        super().__init__(first, last, pay, hours_worked)

    def apply_bonus(self):
        self.pay = int(self.pay * self.bonus)


test1 = Employee('Roger', 'Ramjet', 50000, 35)
dev1 = Developer('Alan', 'Turing', 33000, 65, 'Python')
exec1 = Executive('David', 'Thorn', 100000, 70)

print(Developer.langs()) # example of calling class attribute.

print(f'\ntest: {test1.pay}\ndev: {dev1.pay}\nexec: {exec1.pay}')
print('applying raises and bonuses.')
test1.apply_raise()
dev1.apply_raise()
exec1.apply_bonus()
print(f'test: {test1.pay}\ndev: {dev1.pay}\nexec: {exec1.pay}')
print()
print(exec1)  # shows the __str__, if set will take precendence over __repr__
print(exec1.__repr__())  # how to override __str__ to get __repr__
print()
print(dev1.first)
dev1.first = 'Mickey'
print(dev1.email)  # set as property
# print(dev1.fullname())  # method call '()' prior being made a property
print(dev1.fullname)
print('changing the fullname...\n')
dev1.fullname = 'John Cooper'
print(dev1.fullname)
print(dev1.email)
print()
print('deleter in action...')
del dev1.fullname  # first and last are now None...
