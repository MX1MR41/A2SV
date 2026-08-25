def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True

def solve(n):
    primes = 0
    for num in range(1, n + 1):
        factors = set()
        for i in range(2, num):
            if num % i == 0 and prime(i):
                factors.add(i)
                
                if len(factors) > 2:
                    break

        if len(factors) == 2:
            primes += 1
            
    return primes

n = int(input())
res = solve(n)
print(res)
