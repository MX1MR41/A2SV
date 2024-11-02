t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(input().strip())
    
    zeros, ones = 0, 0
    possible = True
    
    
    for i in range(k):
        tmp = -1
        for j in range(i, n, k):
            if s[j] != '?':
                current_bit = int(s[j])
                if tmp != -1 and current_bit != tmp:
                    possible = False
                    break
                tmp = current_bit
        
        
        if tmp != -1:
            if tmp == 0:
                zeros += 1
            else:
                ones += 1
    
    
    if max(zeros, ones) > k // 2:
        possible = False
    
    print("YES" if possible else "NO")
