import sys, threading

input = lambda: sys.stdin.readline().strip()

def merge(arr):
    res = 0
    n = len(arr)
    if n <= 1: return [arr, 0]

    mid = n//2
    left_half, l_res = merge(arr[:mid])
    right_half, r_res = merge(arr[mid:])
    res += r_res + l_res

    if right_half[0] < left_half[0]:
        res += 1
        return [right_half + left_half, res]
    else:
        return [left_half + right_half, res]



    


def main():
    for _ in range(int(input())):
        flag = False
        n = int(input())
        arr = list(map(int, input().split()))

        arr, res = merge(arr)

        for i in range(1,n):
            if arr[i] < arr[i-1]:
                flag = True
                break
        if flag: print(-1)
        else: print(res)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()