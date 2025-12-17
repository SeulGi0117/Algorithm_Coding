import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if not visited[nr][nc] and grid[nr][nc] == '#':
                        visited[nr][nc] = True
                        q.append((nr, nc))

    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                count += 1
                bfs(i, j)

    print(count)