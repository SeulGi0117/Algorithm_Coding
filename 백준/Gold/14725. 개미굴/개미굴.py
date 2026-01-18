import sys
input = sys.stdin.readline

N = int(input().strip())

trie = {}

for _ in range(N):
    parts = input().split()
    k = int(parts[0])
    foods = parts[1:]

    cur = trie
    for f in foods:
        if f not in cur:
            cur[f] = {}
        cur = cur[f]

def dfs(node: dict, depth: int):
    for key in sorted(node.keys()):
        print("--" * depth + key)
        dfs(node[key], depth + 1)

dfs(trie, 0)