"""


PASSED

"""

n, m, k = list(map(int, input().split()))

def find_lane():
    lane = 0
    l, r = 1, n
    while l <= r:
        mid = (l + r)//2


        if k <= (mid)*m*2 :
            lane  = mid
            r = mid - 1
        else:
            l = mid + 1
    return lane

def find_desk(lane):
    prev = (lane - 1)*m*2
    desk = 0
    l, r = 1, m
    while l <= r:
        mid = (l + r)//2


        if k <= prev + (mid)*2 :
            desk  = mid
            r = mid - 1
        else:
            l = mid + 1
    return desk

lane = find_lane()
desk = find_desk(lane)
side = "L" if k%2 else "R"

print(lane, desk, side)