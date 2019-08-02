#!python3
"""
FizzBuzz

Rules:

1. multiples of 3 return 'Fizz'
2. multiples of 5 return 'Buzz'
3. multiples of both return 'FizzBuzz'

"""

def main():
    plain_range()
    enum_range()

def plain_range():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{i}: FizzBuzz')
        elif i % 3 == 0:
            print(f'{i}: Fizz')
        elif i % 5 == 0:
            print(f'{i}: Buzz')
        else:
            print(f'{i}: ')


def enum_range():
    for k, v in enumerate(range(0, 101)):
        if k % 3 == 0 and k % 5 == 0:
            print(k, "FizzBuzz")
        elif k % 3 == 0:
            print(k, "Fizz")
        elif k % 5 == 0:
            print(k, "Buzz")
        else:
            continue

if __name__ == '__main__':
    main()