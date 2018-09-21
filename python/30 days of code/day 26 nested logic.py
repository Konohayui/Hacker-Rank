# Enter your code here. Read input from STDIN. Print output to STDOUT

act_d, act_m, act_y = map(int, input().strip().split(' '))
exp_d, exp_m, exp_y = map(int, input().strip().split(' '))

if act_y > exp_y:
    print(10000)
elif act_m > exp_m and act_y == exp_y:
    print(500*(act_m - exp_m))
elif act_d > exp_d and act_m == exp_m and act_y == exp_y:
    print(15*(act_d - exp_d))
else:
    print(0)


