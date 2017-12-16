#!python3

# is multiple of 3 return 'Fizz'
# is multiple of 5 return 'Buzz'
# is multiple of both return 'FizzBuzz'

for i in range(101):
    if i % 3 == 0 and i % 5 ==0:
        print(f'{i}: FizzBuzz')
    elif i % 3 == 0:
        print(f'{i}: Fizz')
    elif i % 5 == 0:
        print(f'{i}: Buzz')

