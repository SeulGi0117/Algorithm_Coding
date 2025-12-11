import sys
from collections import deque

def bfs(graph, start, visited, dist):
    queue = deque([start])
    visited[start] = True
    dist[start] = 1  # 시작 포함

    while queue:
        v = queue.popleft()

        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                dist[nxt] = dist[v] + 1
                queue.append(nxt)


input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]

total = N*M
graph = [[] for _ in range(total)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 그래프 생성
for x in range(N):
    for y in range(M):
        if maze[x][y] == 1:
            node = x*M + y
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                    graph[node].append(nx*M + ny)

visited = [False] * total
dist = [0] * total

start = 0
end = total - 1

bfs(graph, start, visited, dist)

print(dist[end])