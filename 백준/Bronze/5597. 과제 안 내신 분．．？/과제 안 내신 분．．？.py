import sys

list_num = []
list_result = []
for _ in range(28):
    n = int(sys.stdin.readline())
    list_num.append(n)

list_num.sort()
for i in range(1, 31):
    if i not in list_num:
        print(i)