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

odds, size = map(int, input().strip().split( ))

total_probability_1 = sum([binomial_dist(i, size, float(odds/100)) for i in range(0, 3)])
total_probability_2 = sum([binomial_dist(i, size, float(odds/100)) for i in range(2, size + 1)])

print(round(total_probability_1, 3))
print(round(total_probability_2, 3))
