import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
campus = [list(input().strip()) for _ in range(N)]

sx = sy = -1
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            sx, sy = i, j
            break
    if sx != -1:
        break

visited = [[False] * M for _ in range(N)]
q = deque()
q.append((sx, sy))
visited[sx][sy] = True

cnt = 0
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    x, y = q.popleft()

    if campus[x][y] == 'P':
        cnt += 1

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and campus[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx, ny))

print(cnt if cnt > 0 else "TT")