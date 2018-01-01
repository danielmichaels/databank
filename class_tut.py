#!/usr/bin/env python3


class Employee:
    """Base class for Employee object."""

    raise_percentage = 1.04  # Class Attribute - it will remain constant across the whole class

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


class Developer(Employee):
    """Developer class."""

    def __init__(self, first, last, pay, hours_worked, language='Python'):
        super().__init__(first, last, pay, hours_worked)
        # super takes the parents
        self.language = language


class Executive(Employee):
    """Executive class."""
    def __init__(self, first, last, pay, hours_worked, bonus=None):
        super().__init__(first, last, pay, hours_worked)
        self.bonus = bonus

    def apply_bonus(self):
        self.bonus = int(self.pay * self.bonus)


test1 = Employee('Roger', 'Ramjet', 50000, 35)
dev1 = Developer('Alan', 'Turing', 33000, 65)
exec1 = Executive('David', 'Thorn', 100000, 70, 1.3)
print(test1.email)
print(dev1.fullname())
print(test1.pay)
print(test1.hours_worked)
print(test1.fullname())
test1.apply_raise()
dev1.apply_raise()

print(test1.pay)
print(dev1.pay)
dev1.language = 'Scala'
print(dev1.language)
print(f'exec without bonus {exec1.pay}')
print(exec1.bonus)
exec1.apply_bonus()
print(f'wtih bonus: {exec1.pay}')
