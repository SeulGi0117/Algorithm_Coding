import sys

n = int(sys.stdin.readline())
changes = 1000 - n
won = [500, 100, 50, 10, 5, 1]
result = 0

for w in won:
    cnt = changes// w
    result += cnt
    changes%=w

print(result)