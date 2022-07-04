import math

def get_gcd(a,b):
    m = a
    n = b
    while not a==b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a

print("Enter two integers")

c,d = map(int, input().split())
print(get_gcd(c,d))
