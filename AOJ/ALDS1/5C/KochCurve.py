import math


def calc_koch_curve(left, right, i):
    if i == n:
        return
    mid1 = (2*left[0] + right[0]) / 3, (2*left[1] + right[1]) / 3
    mid2 = (left[0] + 2*right[0]) / 3, (left[1] + 2*right[1]) / 3
    mid3_x = (
        (mid2[0] - mid1[0]) * math.cos(math.pi/3)
        - (mid2[1] - mid1[1]) * math.sin(math.pi/3) + mid1[0])
    mid3_y = (
        (mid2[0] - mid1[0]) * math.sin(math.pi/3)
        + (mid2[1] - mid1[1]) * math.cos(math.pi/3) + mid1[1])
    mid3 = (mid3_x, mid3_y)

    calc_koch_curve(left, mid1, i+1)
    print(*mid1)
    calc_koch_curve(mid1, mid3, i+1)
    print(*mid3)
    calc_koch_curve(mid3, mid2, i+1)
    print(*mid2)
    calc_koch_curve(mid2, right, i+1)


def main():
    global C
    global n
    C = [(0, 0)]
    n = int(input())
    print(0., 0.)
    calc_koch_curve((0, 0), (100, 0), 0)
    print(100., 0.)


if __name__ == "__main__":
    main()
