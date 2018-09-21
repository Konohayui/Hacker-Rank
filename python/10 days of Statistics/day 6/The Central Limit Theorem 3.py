# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt

samples, mu, sigma, z_score = 100, 500, 80, 1.96

margin_of_error = z_score*sigma/sqrt(samples)
print(round(mu - margin_of_error, 2))
print(round(mu + margin_of_error, 2))
