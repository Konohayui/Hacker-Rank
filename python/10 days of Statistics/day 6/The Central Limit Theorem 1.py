# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import erf, sqrt

def normal_cdf(x, mu, sigma):
    return 0.5*(1 + erf((x - mu)/(sigma*(sqrt(2)))))
    
max_weight, boxes, mu, sigma = 9800, 49, 205, 15
mu_p, sigma_p = boxes*mu, sqrt(boxes)*sigma

proba = round(normal_cdf(max_weight, mu_p, sigma_p), 4)
print(proba)
