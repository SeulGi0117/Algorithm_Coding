import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

if len(A) < len(B):
    A, B = B, A

m = len(B)
prev = [0] * (m + 1)
ans = 0

for i in range(1, len(A) + 1):
    cur = [0] * (m + 1)
    ai = A[i - 1]
    for j in range(1, m + 1):
        if ai == B[j - 1]:
            cur[j] = prev[j - 1] + 1
            if cur[j] > ans:
                ans = cur[j]
    prev = cur

print(ans)