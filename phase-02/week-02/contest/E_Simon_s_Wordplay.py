"""

https://codeforces.com/gym/495129/problem/E
"""

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    
    for i in range(n):
        arr.append(input())
        
    ans = 0
    
    #for each character(a,b,c,d,e)
    for j in range(5):
        char_count = []
        char = chr(ord('a') + j)
    
        for word in arr:
            char_count.append(2*(word.count(char)) - len(word))
        
        char_count.sort(reverse=True)
  
        if char_count[0] <= 0:
            continue
        
        total = char_count[0]
        i = 1
        while i < len(char_count) and total + char_count[i] > 0:
            total += char_count[i]
            i += 1
        
        ans = max(ans,i)
    print(ans)