#!/usr/bin/env python3

import sqlite3


class Employee(object):
    """Here to help illustrate Sqlite3 capabilities"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


def insert_emp(emp):
    with conn:
        cur.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                    {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emp_by_name(lastname):
    cur.execute("SELECT * FROM employees WHERE last=:last",
                {'last': lastname})
    return cur.fetchall()


def update_pay(emp, pay):
    with conn:
        cur.execute("""UPDATE employees SET pay = :pay WHERE first = :first
                      AND last = :last""",
                    {'first': emp.first, 'last': emp.last, 'pay': pay})
    pass


def remove_emp(emp):
    with conn:
        cur.execute(
            "DELETE FROM employees WHERE first = :first AND last = :last",
            {'first': emp.first, 'last': emp.last})


conn = sqlite3.connect(':memory:')  # how to make DB in memory only.
# conn = sqlite3.connect('employee.db')  # connects to db file or creates one.

cur = conn.cursor()  # cursor object allows for interaction with databases.

conn.execute("""CREATE TABLE employees(
    first TEXT,
    last TEXT,
    pay INTEGER
) """)  # """ causes issues in pycharm, definately not PEP8 compliant.

emp_1 = Employee('Rebecca', 'Rabbit', 84500)
emp_2 = Employee('Mrs', 'Rabbit', 94500)


insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emp_by_name('Rabbit')
print(emps)

update_pay(emp_2, 1000000)
remove_emp((emp_1))

emps = get_emp_by_name('Rabbit')
print(emps)

# two different ways to insert into:
# below is the traditional method but not very explicit.
#cur.execute("INSERT  INTO employees VALUES (?,?,?)",
#            (emp_1.first, emp_1.last, emp_1.pay))
## this is a very explicit insert and readable.
#cur.execute("INSERT  INTO employees VALUES (:first, :last, :pay)",
#            {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
#
## selecting when using the ? placeholder.
#cur.execute("SELECT * FROM employees WHERE last=?", ('Rabbit',))  # tuple
## selecting with the dictionary; very easy to read.
#cur.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Rabbit'})
#
## print(cur.fetchone()) # rtn next row.
# print(cur.fetchall())  # rtn remaining, or all rows in list.
# print(cur.fetchmany(5)) # takes arg int, rtns int as list.

conn.commit()

conn.close()
