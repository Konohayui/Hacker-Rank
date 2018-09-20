# Enter your code here. Read input from STDIN. Print output to STDOUT

def fact(n):
    if n == 0:
        return 1
    return n*fact(n - 1)

def binomial_dist(x, n, p):
    p = p
    q = 1 - p 
    comb = fact(n)/(fact(x)*(fact(n- x)))

    return comb*(p**x)*(q**(n - x))

b, g = map(float, input().strip().split( ))

total_probability = sum([binomial_dist(i, 6, b/(b + g)) for i in range(3, 7)])
print(round(total_probability, 3))
