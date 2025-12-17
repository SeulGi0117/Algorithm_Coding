import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 1

def bfs(sr, sc):
    q = deque([(sr, sc)])
    grid[sr][sc] = 0
    size = 1

    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1:
                grid[nr][nc] = 0
                size += 1
                q.append((nr, nc))

    return size

ans = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            ans = max(ans, bfs(i, j))

print(ans)