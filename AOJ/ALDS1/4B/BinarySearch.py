def binary_search(A, q):
    left = -1
    right = len(A)

    while (right - left) > 1:
        mid = (left + right) // 2 
        if q >= A[mid]:
            left = mid
        else:
            right = mid

    if A[left] == q:
        return True

    else:
        return False


def main():
    _ = int(input())
    S = list(map(int, input().split()))
    _ = int(input())
    T = list(map(int, input().split()))
    cnt = 0
    for t in T:
        if binary_search(S, t):
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
