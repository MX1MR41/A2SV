"""

https://codeforces.com/gym/535749/problem/A

PASSED
"""

def points(p, t):
    return max((3*p)/10, p - (p*t)/250)
    
a, b, c, d = list(map(int, input().split()))
misha = points(a,c)
vasya = points(b,d)

if misha > vasya:
    print("Misha")
elif misha < vasya:
    print("Vasya")
else:
    print("Tie")