def main():
    N = int(input())
    p = []
    for i in range(N):
        a, b = map(int, input().split())
        p.append(a)
    else:
        p.append(b)

    m = [[1e10]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        m[i][i] = 0

    for l in range(2, N+1):
        for i in range(1, N-l+2):
            j = i + l - 1

            m[i][j] = 1e10
            for k in range(i, j):
                m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j])

    print(m[1][N])


if __name__ == '__main__':
    main()
