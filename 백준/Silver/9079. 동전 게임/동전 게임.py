import sys

input = sys.stdin.readline

ALL_T = (1 << 9) - 1
ALL_H = 0

def popcount(x: int) -> int:
    return x.bit_count()

ops = []

for r in range(3):
    m = 0
    for c in range(3):
        idx = r * 3 + c
        m |= (1 << idx)
    ops.append(m)

for c in range(3):
    m = 0
    for r in range(3):
        idx = r * 3 + c
        m |= (1 << idx)
    ops.append(m)

diag1 = (1 << 0) | (1 << 4) | (1 << 8)
diag2 = (1 << 2) | (1 << 4) | (1 << 6)
ops.append(diag1)
ops.append(diag2)

def parse_board() -> int:
    state = 0
    for r in range(3):
        row = input().split()
        for c in range(3):
            if row[c] == 'T':
                idx = r * 3 + c
                state |= (1 << idx)
    return state

T = int(input())
out = []
for _ in range(T):
    start = parse_board()
    best = 10**9

    for mask in range(1 << 8):
        cur = start
        for i in range(8):
            if (mask >> i) & 1:
                cur ^= ops[i]

        if cur == ALL_H or cur == ALL_T:
            best = min(best, popcount(mask))

    out.append(str(best if best != 10**9 else -1))

print("\n".join(out))