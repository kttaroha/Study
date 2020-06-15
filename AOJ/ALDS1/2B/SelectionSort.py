def selectionSort(A, N):
    cnt = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if minj != i:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp
            cnt += 1

    print(*A)
    print(cnt)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    selectionSort(A, N)


if __name__ == '__main__':
    main()
