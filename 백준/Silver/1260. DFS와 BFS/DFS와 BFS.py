from collections import deque

def DFS(start):
    # 첫 시작 방문 처리
    dfs_visited[start] = True
    print(start, end=' ')
    # V와 연결되어 있으면서 방문하지 않으면 이 정점을 시작으로 다시 dfs 호출
    for i in graph[start]:
        if not dfs_visited[i]:
            DFS(i)

def BFS(start):
    q = deque([start])
    # 첫 시작 방문처리
    bfs_visited[start] = True

    while q: # Q가 빌 때까지 실행
        v = q.popleft() # queue에 들어있는 값을 꺼냄
        print(v, end=' ')
        for i in graph[v]:
            # i를 방문하지 않고 V와 연결되어 있으면 i값을 추가하고 i값 방문처리
            if not bfs_visited[i]:
                bfs_visited[i] = True
                q.append(i)



# 정점의 개수 N
# 간선의 개수 M
# 탐색을 시작할 정점의 번호 V
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs_visited = [False] * (N+1)
DFS(V)
print()

bfs_visited = [False] * (N+1)
BFS(V)

