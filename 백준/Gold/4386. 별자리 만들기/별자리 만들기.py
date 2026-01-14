import sys
import math

input = sys.stdin.readline

n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]

INF = float('inf')
dist = [INF] * n
visited = [False] * n

dist[0] = 0.0
ans = 0.0

for _ in range(n):
    u = -1
    best = INF
    for i in range(n):
        if not visited[i] and dist[i] < best:
            best = dist[i]
            u = i

    visited[u] = True
    ans += best

    x1, y1 = stars[u]
    for v in range(n):
        if not visited[v]:
            x2, y2 = stars[v]
            w = math.hypot(x1 - x2, y1 - y2)  # sqrt((dx)^2 + (dy)^2)
            if w < dist[v]:
                dist[v] = w

print(ans)