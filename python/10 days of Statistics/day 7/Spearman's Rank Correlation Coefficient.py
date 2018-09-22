# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_rank(array):
    rank = dict((x, r + 1) for r, x in enumerate(sorted(array)))
    return [rank[x] for x in array]

n = int(input())
array_x = list(map(float, input().strip().split( )))
array_y = list(map(float, input().strip().split( )))

rx = get_rank(array_x)
ry = get_rank(array_y)

d = sum([(x - y)**2 for x, y in zip(rx, ry)])

rxy = 1 - (6*d)/(n*(n**2 - 1))
print(round(rxy, 3))
