"""

https://codeforces.com/gym/524965/problem/C

"""

def generate_palindromic_numbers():
    coins = []
    for i in range(1, 4 * 10000 + 4):
        num = str(i)
        if num == num[::-1]:
            coins.append(i)
    
    return coins

coins = generate_palindromic_numbers()
max_num = 4 * 10 ** 4 + 2
mod = 10 ** 9 + 7
dp = [0] * (max_num)
dp[0] = 1

#compute outside because we don’t really have to compute it again and again 
for coin in coins:
    for i in range(max_num):
        if i - coin >= 0:
            dp[i] += dp[i - coin] 
            dp[i] %= mod

#for each test case output dp[n]       
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])