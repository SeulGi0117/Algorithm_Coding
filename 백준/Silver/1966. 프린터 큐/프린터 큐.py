from collections import deque

def printer_queue(n, m, priorities):
    queue = deque([(i, p) for i, p in enumerate(priorities)])  # (문서번호, 중요도)
    count = 0

    while queue:
        cur = queue.popleft()
        # 현재 문서보다 높은 중요도가 하나라도 있으면 뒤로 보내기
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[0] == m:  # 내가 찾는 문서라면
                return count

t = int(input())  # 테스트케이스 개수
for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    print(printer_queue(n, m, priorities))