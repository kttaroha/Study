from collections import deque


def main():
    n = int(input())
    trees = [[] for _ in range(n)]
    sibs = [-1 for _ in range(n)]
    for i in range(n):
        tree = list(map(int, input().split()))
        # trees[tree[0]] = tree[1:]
        if tree[1] != -1 and tree[2] != -1:
            trees[tree[0]] = tree[1:]
            sibs[tree[1]] = tree[2]
            sibs[tree[2]] = tree[1]
        elif tree[1] != -1:
            trees[tree[0]].append(tree[1])
            sibs[tree[1]] = -1
        elif tree[2] != -1:
            trees[tree[0]].append(tree[2])
            sibs[tree[2]] = -1

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
    leaf_node = []
    heights = [0]*n

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
            if not len(trees[t]):
                leaf_node.append(t)

    for l in leaf_node:
        v = l
        height = 0
        while v != -1:
            heights[v] = max(heights[v], height)
            height += 1
            v = parents[v]

    for i in range(n):
        if not depth[i]:
            print(
                "node {}: parent = {}, sibling = {}, degree = {},\
                 depth = {}, height = {}, root"
                .format(
                    i, parents[i], sibs[i],
                    len(trees[i]), depth[i], heights[i])
                )
        elif depth and len(trees[i]):
            print(
                "node {}: parent = {}, sibling = {}, degree = {}, \
                depth = {}, height = {}, internal node"
                .format(
                    i, parents[i], sibs[i],
                    len(trees[i]), depth[i], heights[i]))
        else:
            print(
                "node {}: parent = {}, sibling = {}, degree = 0, \
                depth = {}, height = {}, leaf"
                .format(
                    i, parents[i], sibs[i], depth[i], heights[i]))


if __name__ == '__main__':
    main()
