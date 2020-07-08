def main():
    V, E = map(int, input().split())
    G = [[float("INF")] * V for _ in range(V)]
    for i in range(V):
        G[i][i] = 0
    for _ in range(E):
        s, t, d = map(int, input().split())
        G[s][t] = d

    for k in range(V):
        for i in range(V):
            for j in range(V):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j]) 

    for i in range(V):
        if G[i][i] < 0:
            print("NEGATIVE CYCLE")
            return

        for j in range(V):
            if G[i][j] == float("INF"):
                G[i][j] = "INF"
    for g in G:
        print(*g)


if __name__ == '__main__':
    main()
