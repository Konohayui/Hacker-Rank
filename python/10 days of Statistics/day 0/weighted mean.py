n = int(input())

items = [int(i) for i in input().strip().split( )]
occur = [int(i) for i in input().strip().split( )]

weight_sum = sum([i*o for i, o in zip(items, occur)])
print(round(weight_sum/sum(occur), 1))
