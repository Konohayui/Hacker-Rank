# Enter your code here. Read input from STDIN. Print output to STDOUT

lam_X, lam_Y = map(float, input().strip().split( ))

expect_A = 160 + 40*(lam_X + lam_X**2)
expect_B = 128 + 40*(lam_Y + lam_Y**2)

print(round(expect_A, 3))
print(round(expect_B, 3))
