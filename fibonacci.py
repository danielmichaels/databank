#!python3

def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

print("Fibonacci's 0-10")
fib(10)
print("Now 0-5")
fib(5)
