"""

https://codeforces.com/gym/522079/problem/A

PASSED
"""

vow = set(["a", "e", "i", "o", "u", "y"])
n = int(input())
s = list(input())


while True:
    # print(s)
    flag = True
    for i in range(n-1):
        if s[i] in vow and s[i+1] in vow:
            s.pop(i+1)
            n -= 1
            flag = False
            break

    if flag: 
        print("".join(s))
        exit()



        
