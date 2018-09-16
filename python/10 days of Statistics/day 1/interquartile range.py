# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_median(array):
    n = len(array)
    if n % 2 == 0:
        return sum(array[n//2 - 1:n//2 + 1])/2
    else:
        return array[n//2]


n = int(input())

items = [int(i) for i in input().strip().split( )]
freq = [int(i) for i in input().strip().split( )]

full_array = []
for i in range(n):
    full_array += [items[i]] * freq[i]

full_array = sorted(full_array)

N = sum(freq)

if n % 2 == 0:
    Q1 = get_median(full_array[:N//2])
    Q3 = get_median(full_array[N//2:])

else:
    Q1 = get_median(full_array[:N//2])
    Q3 = get_median(full_array[N//2 + 1:])

print(round(float(Q3 - Q1), 1))

