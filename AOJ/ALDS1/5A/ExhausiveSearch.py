def solve(i, m):

    if i >= n:
        combs.add(m)
        return

    solve(i+1, m)
    solve(i+1, m+A[i])


def main():
    global n
    global A
    global combs
    n = int(input())
    A = list(map(int, input().split()))
    _ = int(input())
    Q = list(map(int, input().split()))
    # 先に全部の組み合わせを計算しておくことで時間短縮
    combs = set()
    solve(0, 0)

    for q in Q:
        if q in combs:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    main()
