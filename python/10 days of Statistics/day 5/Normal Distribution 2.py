# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf, sqrt

def normal_cdf(x, mu, sigma):
    return 0.5*(1 + erf((x - mu)/(sigma*(sqrt(2)))))

mu, sigma = 70, 10

second_high = 1 - normal_cdf(80, mu, sigma)
passed = 1 - normal_cdf(60, mu, sigma)
failed = 1 - passed

print(round(second_high*100, 2))
print(round(passed*100, 2))
print(round(failed*100, 2))
