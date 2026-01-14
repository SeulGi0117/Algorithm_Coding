import sys
input = sys.stdin.readline

n = int(input().strip())
tree = {}

for _ in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)

pre = []
ino = []
post = []

def preorder(x):
    if x == '.':
        return
    l, r = tree[x]
    pre.append(x)
    preorder(l)
    preorder(r)

def inorder(x):
    if x == '.':
        return
    l, r = tree[x]
    inorder(l)
    ino.append(x)
    inorder(r)

def postorder(x):
    if x == '.':
        return
    l, r = tree[x]
    postorder(l)
    postorder(r)
    post.append(x)

root = 'A'
preorder(root)
inorder(root)
postorder(root)

print(''.join(pre))
print(''.join(ino))
print(''.join(post))