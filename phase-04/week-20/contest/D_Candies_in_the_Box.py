def check_k(n, k):
    eaten = 0 
    curr_candies = n 
    while curr_candies > 0:
        k = min(k, curr_candies)
        eaten += k 
        curr_candies -= k
        curr_candies -= curr_candies // 10 
    
    return eaten * 2 >= n 

n = int(input())
k = n
left, right = 1, n 
while left <= right:
    mid = left + (right - left) // 2
    if check_k(n, mid):
        k = mid 
        right = mid - 1
    else:
        left = mid + 1

print(k)