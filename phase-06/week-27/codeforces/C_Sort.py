# https://codeforces.com/contest/1996/problem/C

# store the prefix sum of each letter at each index, as an array of size 26

for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    a = input()
    b = input()

    def count(d1, d2):
        matches = 0

        for i in range(26):
            matches += min(d1[i], d2[i])
        
        return matches


    a_pre = []
    b_pre = []

    a_cnt = [0] * 26
    b_cnt = [0] * 26

    for i in range(n):
        a_cnt[ord(a[i]) - 97] += 1
        b_cnt[ord(b[i]) - 97] += 1

        a_pre.append(a_cnt[::])
        b_pre.append(b_cnt[::])

    

    for _ in range(q):
        l, r = list(map(int, input().split()))
        l -= 1
        r -= 1

        if l == 0:
            res = (r - l + 1) - count(a_pre[r], b_pre[r])

        else:
            
            a_left, a_right = a_pre[l - 1], a_pre[r]
            d1 = a_right[::]
            for i in range(26):
                d1[i] -= a_left[i]

            b_left, b_right = b_pre[l - 1], b_pre[r]
            d2 = b_right[::]
            for i in range(26):
                d2[i] -= b_left[i]
            

            res = (r - l + 1) - count(d1, d2)

        print(res)

    
