# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

array = [int(i) for i in input().strip().split( )]

def get_std(array, n):
    mean = sum(array)/n
    array = [(x - mean)**2 for x in array]
    return round((sum(array)/n)**(1/2), 1)

print(get_std(array, n))
