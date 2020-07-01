def fib(n):
    nums = []
    for i in range(n+1):
        if i <= 1:
            nums.append(1)
        else:
            nums.append(nums[i-1]+nums[i-2])
    return nums[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
