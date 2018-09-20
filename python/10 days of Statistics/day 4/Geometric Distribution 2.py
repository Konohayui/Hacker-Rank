# Enter your code here. Read input from STDIN. Print output to STDOUT

def geo_dist(n, p):
    p = p
    q = 1 - p 

    return p*(q**(n - 1))

n, m = map(int, input().strip().split( ))
trails = int(input())
p = n/m

total_probability = sum([geo_dist(i, p) for i in range(1, trails + 1)])

print(round(total_probability, 3))
