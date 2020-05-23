from collections import deque


def main():
    n = int(input())
    trees = [None for _ in range(n)]
    for i in range(n):
        tree = list(map(int, input().split()))
        trees[tree[0]] = tree[2:]

    # 根を探す
    candidates = set()
    have_parents = set()
    children = []
    for i in range(len(trees)):
        if len(trees[i]):
            candidates.add(i)
            children.extend(trees[i])
    children = set(children)
    have_parents = {c for c in candidates if c in children}

    if n == 1:
        root_node = 0
    else:
        root_node = list(candidates - have_parents)[0]

    depth = []
    q = deque()
    seen = [0]*n
    depth = [0]*n
    parents = [0]*n

    q.append(root_node)
    seen[root_node] = 1
    parents[root_node] = -1

    # DFS
    while len(q):
        v = q.pop()
        d = depth[v] + 1
        for t in trees[v]:
            if seen[t]:
                continue
            seen[t] += 1
            parents[t] = v
            q.append(t)
            depth[t] = d

    for i in range(n):
        if not depth[i]:
            print(
                "node {}: parent = {}, depth = {}, root, {}"
                .format(i, parents[i], depth[i], trees[i]))
        elif depth and len(trees[i]):
            print(
                "node {}: parent = {}, depth = {}, internal node, {}"
                .format(i, parents[i], depth[i], trees[i]))
        else:
            print(
                "node {}: parent = {}, depth = {}, leaf, {}"
                .format(i, parents[i], depth[i], trees[i]))


if __name__ == '__main__':
    main()
