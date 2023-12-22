"""
https://codeforces.com/gym/493037/problem/E

FAILED
"""


def count_sub_str(s,v):
    ans = 0
    for i in range(len(s)-6):
        if s[i:i+7] == v: ans += 1
    return ans
 
def solve():
    n = int(input())
    s = input()
    sub_str = "abacaba"

    if count_sub_str(s,sub_str) == 1:
        s = s.replace('?','x')
        print("YES")
        print(s)
        return
   
    for i in range(n-6):
        cur = list(s)

        for x in range(i,i+7):
            if cur[x] == '?':
                cur[x] = sub_str[x - i]

        cur = "".join(cur)
        if count_sub_str(cur,sub_str) == 1:
            cur = cur.replace('?','x')
            print("YES")
            print(cur)
            return
       
    print("NO")
 
T = int(input())
for _ in range(T):
    solve()