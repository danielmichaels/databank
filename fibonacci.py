#!python3

def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

fib(10)
