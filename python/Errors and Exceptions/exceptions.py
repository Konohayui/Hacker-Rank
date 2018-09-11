for _ in range(int(input())):
    a, b = input().strip().split()
    try:
        print(int(a)//int(b))
    except Exception as e:
        print("Error Code:", e)

