# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import erf, sqrt

def normal_cdf(x, mu, sigma):
    return 0.5*(1 + erf((x - mu)/(sigma*(sqrt(2)))))
    
total_tickets, students, mu, sigma = 250, 100, 2.4, 2.0
mu_p, sigma_p = students*mu, sqrt(students)*sigma

proba = round(normal_cdf(total_tickets, mu_p, sigma_p), 4)
print(proba)
