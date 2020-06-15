def insertionSort(A, N):
    for i in range(N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print(*A)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    insertionSort(A, N)


if __name__ == '__main__':
    main()
