# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
array_x = list(map(float, input().strip().split( )))
array_y = list(map(float, input().strip().split( )))

mu_x = sum(array_x)/n
mu_y = sum(array_y)/n

sigma_x = (sum([(x - mu_x)**2 for x in array_x])/n)**(1/2)
sigma_y = (sum([(y - mu_y)**2 for y in array_y])/n)**(1/2)

cov = sum([(x - mu_x)*(y - mu_y) for x, y in zip(array_x, array_y)])/n
corr = round(cov/(sigma_x*sigma_y), 3)
print(corr)
