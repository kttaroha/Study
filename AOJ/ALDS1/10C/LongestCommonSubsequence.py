from sys import stdin


def main():
    q = int(stdin.readline().rstrip())
    for _ in range(q):
        X = list(stdin.readline().rstrip())
        Y = list(stdin.readline().rstrip())
        dp = [[0] * (len(Y)+1) for _ in range(len(X)+1)]
        for i in range(len(X)):
            for j in range(len(Y)):
                if X[i] == Y[j]:
                    dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j+1])
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])

        print(dp[-1][-1])


if __name__ == '__main__':
    main()

# こちらじゃないと時間が間に合わない
"""
from sys import stdin

def main():
    q = int(stdin.readline().rstrip())
    for _ in range(q):
        X = list(stdin.readline().rstrip())
        Y = list(stdin.readline().rstrip())
        dp = [0] * (len(Y)+1)
        for i in range(len(X)):
            x = X[i]
            dp_ = dp[:]
            for j in range(len(Y)):
                if x == Y[j]:
                    dp[j+1] = dp_[j] + 1
                elif dp[j+1] < dp[j]:
                    dp[j+1] = dp[j]

        print(dp[-1])


if __name__ == '__main__':
    main()
"""