import sys, threading

input = lambda: sys.stdin.readline().strip()



def destroy(avengers, left, right, A, B):

    if len(avengers) == 0:
        return A
    
    if left == right:
        return B*len(avengers)
    
    power = B*len(avengers)*(right - left + 1)
    first_half = []
    second_half = []

    mid = (left + right)//2

    for av in avengers:
        if av > mid:
            second_half.append(av)

        else:
            first_half.append(av)

    power = min(power, destroy(first_half, left, mid, A, B) + destroy(second_half, mid+1, right, A, B))
    return power


def main():
    n, k, A, B = map(int, input().split())
    a = list(map(int,input().split()))

    a.sort()
    print(destroy(a,1,2**n, A, B))
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
