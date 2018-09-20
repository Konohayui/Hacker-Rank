# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_prime(n):
    if n == 1:
        return "Not prime"
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return "Not prime"
    return "Prime"

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    print(is_prime(n))
