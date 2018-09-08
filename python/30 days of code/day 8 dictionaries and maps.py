n_name = int(input())
book = {}

for _ in range(n_name):
    name, number = input().split()
    book[name] = number
    
for _ in range(n_name):
    name = input()
    if name in book:
        print("{}={}".format(name, book[name]))
    else:
        print("Not found")
