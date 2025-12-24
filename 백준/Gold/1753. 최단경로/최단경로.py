import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split()) # 정점 개수, 간선 개수
K = int(input()) # 시작 정점 번호

# u에서 출발하는 간선들을 담는 리스트
graph = [[] for _ in range(V + 1)]

# 간선 E개 입력받아서 그래프에 저장. u에서 v로 가는 비용이 w
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = float('inf')
dist = [INF] * (V + 1)
dist[K] = 0

# 힙 준비
pq = []
heapq.heappush(pq, (dist[K], K))  # (거리, 정점)

while pq:
    cur_distance, cur = heapq.heappop(pq)
    if cur_distance > dist[cur]:
        continue

    for next_node, w in graph[cur]:
        new_distance = cur_distance + w
        if new_distance < dist[next_node]:
            dist[next_node] = new_distance
            heapq.heappush(pq, (new_distance, next_node))

out = []
# 1번 정점부터 V번 정점가지 출력
for i in range(1, V + 1):
    if dist[i] == INF:
        out.append("INF")
    else:
        out.append(str(dist[i]))
print("\n".join(out))
