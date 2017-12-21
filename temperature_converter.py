#!python3

# write two functions that convert fahrenheit to celsius and back
#   Tc=(5/9)*(Tf-32)
#  Tf=(9/5)*Tc+32
def main():
    printer()
    amount()

def printer():
    print('#' * 40)
    print('\t\t Temperature Converter')
    print('#' * 40)

def to_celsius(n):
    n = (5/9) * (n - 32)
    print(f'Celsius: {n}')


def to_fahrenheit(n):
    n = (9/5) * n + 32
    print(f'Fahrenheit: {n}')

def amount():
    temp = int(input('What temp?: '))
    # temp = float(temp)
    print('Type 1. for Fahrenheit, and 2. for Celsius. Enter to Quit')
    what = (input(' 1. or 2. >>'))

    if what == '1':
        to_fahrenheit(temp)
    elif what == '2':
        to_celsius(temp)
    else:
        print('Exiting..')



if __name__ == '__main__':
    main()

