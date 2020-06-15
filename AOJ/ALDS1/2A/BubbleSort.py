def bubbleSort(A, N):
    flag = 1
    cnt = 0
    while flag:
        flag = 0
        for j in range(N-1, 0, -1):
            if A[j] < A[j-1]:
                cnt += 1
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag = 1
    print(*A)
    print(cnt)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    bubbleSort(A, N)


if __name__ == '__main__':
    main()
