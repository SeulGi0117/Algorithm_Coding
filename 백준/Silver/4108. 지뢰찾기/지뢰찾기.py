import sys

input = sys.stdin.readline

# 8방향 이동 (상, 하, 좌, 우, 대각선 4개)
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break  # 입력 종료

    # 지뢰밭 입력 받기
    board = [list(input().strip()) for _ in range(R)]

    # 결과를 담을 배열 (문자 하나씩 채울 예정)
    result = [[''] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            # 지뢰면 그대로 '*'
            if board[r][c] == '*':
                result[r][c] = '*'
                continue

            # 지뢰가 아니면 주변 8칸의 지뢰 개수 세기
            mine_count = 0
            for k in range(8):
                nr = dr[k] + r
                nc = dc[k] + c

                # 범위 밖이면 건너뜀
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue

                if board[nr][nc] == '*':
                    mine_count += 1

            # 숫자로 채우기 (문자형으로 저장)
            result[r][c] = str(mine_count)

    # 출력 (각 줄을 문자열로 합쳐서 출력)
    for r in range(R):
        print(''.join(result[r]))