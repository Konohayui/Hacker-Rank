# Enter your code here. Read input from STDIN. Print output to STDOUT

def geo_dist(n, p):
    p = p
    q = 1 - p 

    return p*(q**(n - 1))

n, m = map(int, input().strip().split( ))
first = int(input())
p = n/m

probability = geo_dist(first, p)

print(round(probability, 3))
