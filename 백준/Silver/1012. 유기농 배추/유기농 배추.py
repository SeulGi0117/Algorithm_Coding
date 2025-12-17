import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    def bfs(sy, sx):
        q = deque([(sy, sx)])
        field[sy][sx] = 0
        while q:
            y, x = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and field[ny][nx] == 1:
                    field[ny][nx] = 0
                    q.append((ny, nx))

    worms = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                worms += 1
                bfs(y, x)

    print(worms)