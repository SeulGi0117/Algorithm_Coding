import sys
# 입력받기
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))
A.sort()

# 이진 탐색 함수
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

# 각 target에 대해 탐색
for t in targets:
    print(binary_search(A, t))