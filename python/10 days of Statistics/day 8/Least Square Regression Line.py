# Enter your code here. Read input from STDIN. Print output to STDOUT

x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)

n = 0
d = 0

for i in range(len(x)):
    n += (x_mean-x[i])*(y_mean-y[i])
    d += (x_mean-x[i])**2 

slope = n/d
inter = y_mean - slope*x_mean
prediction = slope*80 + inter
print (round(prediction, 3))
