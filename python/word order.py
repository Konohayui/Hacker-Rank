from collections import OrderedDict
result = OrderedDict()

for _ in range(int(input())):
    s = input()
    if s not in result:
        result[s] = 1
    else:
        result[s] += 1
        
print(len(result.keys()))
print(*result.values())
