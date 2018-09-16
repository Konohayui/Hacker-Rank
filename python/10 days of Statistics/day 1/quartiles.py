# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

array = sorted([int(i) for i in input().strip().split( )])

def get_median(array):
    if len(array) % 2 == 0:
        return sum(array[len(array)//2 - 1:len(array)//2 + 1])/2
    else:
        return array[len(array)//2]

def get_quartiles(array, n):
    Q1 = get_median(array[:n//2])
    Q2 = get_median(array)
    if n % 2 == 0:
        Q3 = get_median(array[n//2:])
    else:
        Q3 = get_median(array[n//2 + 1:])

    return Q1, Q2, Q3

Q1, Q2, Q3 = map(int, get_quartiles(array, n))

print(Q1)
print(Q2)
print(Q3)
