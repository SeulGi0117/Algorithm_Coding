import sys

input = sys.stdin.readline

# 상하좌우 대각선 이동방향
# k번째 방향으로 얼마나 이동하는지. range 8돌면 차례대로 모든 방향 검사 가능
direction_r = [-1, -1, -1, 0, 0, 1, 1, 1]
direction_c = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    # 입력받기
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break

    nemo = [list(input().strip()) for _ in range(R)]

    result = [[''] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if nemo[r][c] == '*':
                result[r][c] = '*'
                continue

            # 지뢰 아닐때
            cnt = 0
            for k in range(8):
                nr = direction_r[k] + r
                nc = direction_c[k] + c

                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue

                if nemo[nr][nc] == '*':
                    cnt += 1
            result[r][c] = str(cnt)

    for r in range(R):
        print(''.join(result[r]))