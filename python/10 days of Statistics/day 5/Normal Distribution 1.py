# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf, sqrt

def normal_cdf(x, mu, sigma):
    return 0.5*(1 + erf((x - mu)/(sigma*(sqrt(2)))))

mu, sigma = map(int, input().strip().split( ))
a = float(input())
b, c = map(float, input().strip().split( ))


print(round(normal_cdf(a, mu, sigma), 3))
case_2 = normal_cdf(c, mu, sigma) - normal_cdf(b, mu, sigma)
print(round(case_2, 3))
