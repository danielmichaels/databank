#!/usr/bin/env python3

#TODO: Amortization
"""
It is common for loans to be amortized which allows the lendor to collect their interest early in the loan period. We will ignore amortization
for the purpose of this program. For bonus points, figure out how to do amortization and print an amortization schedule with the payment schedule.
There is an excellent explanation of the amortization formula at Interest.com.

Amortization forumla:

A = p(1 + r)n / (1 + r)n - 1

A = amount per period
p = initial principal
r = interest rate
n = number of payments or periods

Write a program that calculates the interest due on a loan and prints a payment schedule. Make sure you round the output to two decimal places.
For bonus points, figure out how to calculate amortization and print an amortization schedule.
It will be your responsibility to find an appropriate format for the amortization printout.

Sample session

Loan calculator

Amount borrowed: 100
Interest rate: 6
Term (years): 1

Amount borrowed:    $100.00
Total interest paid:  $6.00

           Amount     Remaining
Pymt#       Paid       Balance
-----      -------    ---------
  0        $ 0.00      $106.00
  1        $ 8.84      $ 97.16
  2        $ 8.84      $ 88.32
  3        $ 8.84      $ 79.48
  4        $ 8.84      $ 70.64
  5        $ 8.84      $ 61.80
  6        $ 8.84      $ 52.96
  7        $ 8.84      $ 44.12
  8        $ 8.84      $ 35.28
  9        $ 8.84      $ 26.44
 10        $ 8.84      $ 17.60
 11        $ 8.84      $  8.76
 12        $ 8.76      $  0.00

"""


def main():
    p, r, t = get_info()
    printer(p, r, t)
    calc = calculation(p, r)
    schedule(calc, t)


def printer(p, r, t):
    print()
    print(f'Starting Balance: {p}')
    print(f'Interest Rate: {r * 100}%')
    print(f'Length of contract in months: {t}')
    print()
    print('Pymt#\tAmount Paid\t\tBalance')


def get_info():
    """
    Interrogates the user for Principal, Interest Rate and Length (time) of
    contract.

    p: Principal, r: Interest Rate, t: Time in Months

    :return:
    principal in float, interest rate in float and time (or length) as int.
    r (interest rate) is divided by 100 for better further processing in
    calculation func.
    """

    print()
    print('#' * 40)
    print('Simple Interest Calculator')
    print('#' * 40)
    print()
    p = float(input('What is the Principal? >> '))
    r = float(input(
        'What is your Interest Rate? (in percent i.e \'6.5\' for 6.5% >> '))
    t = int(input('Total length of contract? >> '))

    r = r / 100  # returns something like this: r = R/100 = 5.5%/100 = 0.055)

    return p, r, t


def calculation(p, r):
    """

    :param:
    i = p × r × t
    where i is the interest paid, p is the amount borrowed (principal), r is
    the interest rate, and t is the length of the loan.

    t (time) is removed as the user enters it in get_info.

    :return:
    interest percentage plus the principal in cents.

    """
    i = p * r

    return (i + p) * 100  # put into cents to defeat rounding errors


def schedule(calc, length):
    """
    Given a interest calculation a schedule of repayment can be determined.
    Outputs the minimum repayments for a set time.

    :param calc:
    Takes arg from calculation.
    :param length:
    Give a time to repay will get the minimum repayment. Calculated in Months.

    """
    payment = float(calc) / length
    for i in range(length):
        print(f'\t{i}\t\t{payment / 100:.2f}\t\t{calc / 100:.2f}')
        calc = float(calc) - payment


if __name__ == '__main__':
    main()
