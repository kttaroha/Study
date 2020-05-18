def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if x >= A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]

    return i + 1


def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = partition(A, 0, n-1)
    for i in range(len(A)):
        if i == q:
            A[i] = "[" + str(A[i]) + "]"
        else:
            A[i] = str(A[i])

    print(*A)


if __name__ == "__main__":
    main()
