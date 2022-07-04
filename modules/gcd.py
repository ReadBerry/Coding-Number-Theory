#--Uses Euclid's algorithm to find the greatest common denominator (greatest common factor), or GCD of two positive integers

import math

def get_gcd(a,b):
    m = abs(a)
    n = abs(b)

    while not a==b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a


while 1==1:
    print("Enter two integers")

    try:
        c,d = map(int, input().split())
        print(get_gcd(c,d))
    except:
        print("ERROR | Did you input two integers?")
