def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    num_coins = [0] * (N+1)
    for i in range(N):
        min_num_coins = 1e5
        for a in A:
            if a <= i+1:
                min_num_coins = min(num_coins[i+1-a]+1, min_num_coins)
        num_coins[i+1] = min_num_coins

    print(num_coins[N])


if __name__ == '__main__':
    main()
