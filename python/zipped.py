# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().strip().split( ))

all_scores = []

for _ in range(X):
    all_scores.append([float(i) for i in input().strip().split( )])

for student_score in zip(*all_scores):
    print(round(sum(student_score)/X, 1))
