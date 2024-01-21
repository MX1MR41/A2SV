"""

https://codeforces.com/gym/497696/problem/E

"""

n = int(input())
arr = list(map(int , input().split()))
s , f = map(int , input().split())
 
ans = 1
# The window when time = 1 at first timezone
cur_total = sum(arr[s - 1:f - 1])


left = s - 1 # the leftmost element in our window
right = f - 2 # the rightmost element in our window


max_value = cur_total


for i in range(2 , n + 2):
   
   cur_total -= arr[right]
   right -= 1
   left -= 1  
   # When left and right < 0 that means they start iterating from the back    
   cur_total += arr[left]


   if cur_total > max_value:
       ans = i
       max_value = cur_total
print(ans if ans else n)	