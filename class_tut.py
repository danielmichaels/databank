#!/usr/bin/env python3


class Employee:
    """Base class for Employee object."""

    raise_percentage = 1.04  # Class Attribute

    def __init__(self, first, last, pay, hours_worked):
        self.first = first
        self.last = last
        self.email = first + last + '@email.com'
        # Not taken from __init__ as it is created from two of the arguments.
        self.pay = pay
        self.hours_worked = hours_worked

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_percentage)

    def __repr__(self):
        return 'Employee: {} {}, ${}p.a. , {}'.format(
            self.first, self.last, self.pay, self.email)

    def __str__(self):
        return 'this is the __str__ representation'


class Developer(Employee):
    """Developer class."""

    def __init__(self, first, last, pay, hours_worked, language='Python'):
        super().__init__(first, last, pay, hours_worked)
        # super allows MRO to change dynamically with parent. Delegates method
        # calls to parent/ sibling type. By not naming parent explicitly code
        # is more maintainable.
        self.language = language


class Executive(Employee):
    """Executive class."""

    bonus = 1.07

    def __init__(self, first, last, pay, hours_worked):
        super().__init__(first, last, pay, hours_worked)

    def apply_bonus(self):
        self.pay = int(self.pay * self.bonus)


test1 = Employee('Roger', 'Ramjet', 50000, 35)
dev1 = Developer('Alan', 'Turing', 33000, 65)
exec1 = Executive('David', 'Thorn', 100000, 70)

print(f'test: {test1.pay}\ndev: {dev1.pay}\nexec: {exec1.pay}')
print('applying raises and bonuses.')
test1.apply_raise()
dev1.apply_raise()
exec1.apply_bonus()
print(f'test: {test1.pay}\ndev: {dev1.pay}\nexec: {exec1.pay}')

print(exec1)
