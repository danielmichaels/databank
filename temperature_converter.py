#!python3

# write two functions that convert fahrenheit to celsius and back
#   Tc=(5/9)*(Tf-32)
#  Tf=(9/5)*Tc+32

def to_celsius(n):
    n = (5/9) * (n -32)
    print(n)


def to_fahrenheit(n):
    n = (9/5) * n + 32
    print(n)


to_celsius(50)
to_fahrenheit(30)