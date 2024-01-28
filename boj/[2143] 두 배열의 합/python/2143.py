import sys
from collections import defaultdict

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = [int(x) for x in sys.stdin.readline().split()]
m = int(sys.stdin.readline())
B = [int(x) for x in sys.stdin.readline().split()]
sum_dict = defaultdict(int)
answer = 0

for i, v in enumerate(A):
    for j in range(i, n):
        sum_dict[sum(A[i:j + 1])] += 1
for i, v in enumerate(B):
    for j in range(i, m):
        answer += sum_dict[T - sum(B[i:j + 1])]
print(answer)
