def main():
    m, s = map(int, input().split())
    if s == 0:
        if m == 1:
            print(0, 0)
        else:
            print(-1, -1)
        return
    if m == 1:
        if s >= 0 and s <= 9:
            print(s, s)
        else:
            print(-1, -1)
        return

    def can(m, s):
        return 0 <= s <= 9 * m

    if not can(m, s):
        print(-1, -1)
        return

    minn, maxx = "", ""
    sum_min, sum_max = s, s

    for i in range(m):
        for d in range(10):
            if (i > 0 or d > 0 or (m == 1 and d == 0)) and can(m - i - 1, sum_min - d):
                minn += chr(ord('0') + d)
                sum_min -= d
                break

    for i in range(m):
        for d in range(9, -1, -1):
            if can(m - i - 1, sum_max - d):
                maxx += chr(ord('0') + d)
                sum_max -= d
                break

    print(minn, maxx)

if __name__ == '__main__':
    main()
