from sys import stdin
moves = []

def gcd(a,b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a,b-a)

def gcd2(a,b):
    if a < b:
        
         