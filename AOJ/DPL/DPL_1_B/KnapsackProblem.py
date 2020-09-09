def main():
    N, W = map(int, input().split())
    V = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (W+1) for _ in range(N+1)]

    for i in range(N):
        v, w = V[i][0], V[i][1]
        for j in range(W+1):
            if j >= w:
                dp[i+1][j] = max(dp[i][j-w]+v, dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]

    print(max(dp[N]))


if __name__ == '__main__':
    main()
