n, m = map(int, input().split())
parent = [i for i in range(n+1)]


def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    status, a, b = map(int, input().split())

    if status:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)

    # print('union status : ', parent)
