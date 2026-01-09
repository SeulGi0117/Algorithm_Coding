import sys

input = sys.stdin.readline

N, D = map(int, input().split())
# start가 D 이하인 것만 담기
shortcut = [[] for _ in range(D + 1)]

for _ in range(N):
    start, end, length = map(int, input().split())
    # D를 넘어가는 지름길은 버림. 넘어가면 역주행을 못함
    if end > D:
        continue
    if length >= end - start:
        continue
    if start < D:
        shortcut[start].append((end, length))

INF = float('inf')
dp = [INF] * (D + 1)
dp[0] = 0

for i in range(D):
    dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    for end, length in shortcut[i]:
        dp[end] = min(dp[end], dp[i] + length)

print(dp[D])
