#--Uses Euclid's algorithm to find the greatest common denominator (greatest common factor), or GCD of two positive integers

import math

def get_gcd(a,b):
    m = abs(a)
    n = abs(b)
    try:
        while not a==b:
            if a>b:
                a = a-b
            else:
                b = b-a
        return a
    except:
        print("Did you enter two integers?")

print("Enter two integers")

c,d = map(int, input().split())
print(get_gcd(c,d))
