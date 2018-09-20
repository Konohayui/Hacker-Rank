# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import e 

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def poisson_dist(k, l):
    return (l**k)*(e**(-l))/fact(k)

l = float(input())
k = int(input())

print(round(poisson_dist(k, l), 3))
