import heapq


def main():
    V, E, r = map(int, input().split())
    G = [[] for _ in range(V)]
    P = [1e10]*V
    for _ in range(E):
        s, t, d = map(int, input().split())
        G[s].append((d, t))

    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, r))
    fixed = [0]*V
    while q:
        v = heapq.heappop(q)
        if P[v[1]] > v[0]:
            P[v[1]] = v[0]
        fixed[v[1]] += 1
        for g in G[v[1]]:
            if not fixed[g[1]]:
                dist = g[0] + P[v[1]]
                P[g[1]] = dist
                heapq.heappush(q, (dist, g[1]))

    for p in P:
        if p == 1e10:
            print("INF")
        else:
            print(p)


if __name__ == '__main__':
    main()
