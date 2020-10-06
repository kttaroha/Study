def main():
    inf = 10e5
    n = int(input())
    mats = [list(map(int, input().split())) for _ in range(n)]
    dp = [[inf] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for diff in range(1, n):  # 何個隣の行列との積を計算するか
        for i in range(n-diff):  # 行列積の始点
            j = i + diff  # 行列積の終点

            # 行列iからjの連鎖積を計算している
            # 具体的には行列i~kの積×行列k+1~jの行列積をkをiからj-1まで動かして計算し、
            # 最小のものを計算している
            dp[i][j] = inf
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][k]+dp[k+1][j]+mats[i][0]*mats[k][1]*mats[j][1])
    print(dp[0][n-1])


if __name__ == '__main__':
    main()
