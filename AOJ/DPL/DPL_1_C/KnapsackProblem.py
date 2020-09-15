def main():
    N, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    V = [[0] * (W+1) for _ in range(N+1)]

    for i in range(N):
        v, w = A[i-1][0], A[i-1][1]
        for j in range(W+1):
            if j >= w:
                V[i+1][j] = max((V[i][j], V[i+1][j-w]+v))
            else:
                V[i+1][j] = V[i][j]

    print(max(V[N]))


if __name__ == '__main__':
    main()
