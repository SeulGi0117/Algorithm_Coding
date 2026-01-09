import sys
import heapq

input = sys.stdin.readline
N, T = map(int, input().split())
grass = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dist = [[[INF] * 3 for _ in range(N)] for _ in range(N)]

# 시작은 0,0에서. 이동횟수 0번. -> k=0 출발에선 풀 안먹음
dist[0][0][0] = 0
# (time:r,c에 도착하는데 걸린 최소시간, r, c, k: 지금까지 길 건넌 횟수 mod3 -> 언제 풀먹어야 되는지)
pq = [(0, 0, 0, 0)]

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 상태 그래프 다익스트라
while pq:
    time, r, c, k = heapq.heappop(pq)
    # 이 상태보다 더 빠른 경로가 이미 dist에 있으면 건너뛰기
    if time > dist[r][c][k]:
        continue

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue

        nk = (k + 1) % 3  # 이동하면 건넌 횟수 +1
        nt = time + T  # 길 하나 건너는 시간

        # 풀 뜯어 먹기
        if nk == 0:
            nt += grass[nr][nc]

        if nt < dist[nr][nc][nk]:
            dist[nr][nc][nk] = nt
            heapq.heappush(pq, (nt, nr, nc, nk))
print(min(dist[N - 1][N - 1]))
