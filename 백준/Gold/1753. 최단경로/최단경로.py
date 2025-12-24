import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = float('inf')
dist = [INF] * (V + 1)
dist[K] = 0
pq = []
heapq.heappush(pq, (dist[K], K))  # (거리, 정점)

while pq:
    d, x = heapq.heappop(pq)
    if d != dist[x]:
        continue
    for next_node, w in graph[x]:
        nd = d + w
        if nd < dist[next_node]:
            dist[next_node] = nd
            heapq.heappush(pq, (nd, next_node))
out = []
for i in range(1, V + 1):
    if dist[i] == INF:
        out.append("INF")
    else:
        out.append(str(dist[i]))
print("\n".join(out))
