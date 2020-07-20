def modpow(a, n, mod):
    res = 1
    while n > 0:
        if (n & 1):
            res = res * a % mod
        a = a * a % mod
        n = n >> 1

    return res


def main():
    m, n = map(int, input().split())
    print(modpow(m, n, 1000000007))


if __name__ == "__main__":
    main()
