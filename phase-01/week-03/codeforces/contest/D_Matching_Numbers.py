"""
https://codeforces.com/gym/493037/problem/D

FAILED
"""
from math import ceil
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print("NO")
    else:
        print("YES")
        total = 2 * n
        total_sum = total* (total + 1) // 2
        middle_element = total_sum // n
        starting_number_one = middle_element - n // 2 - 1
        starting_number_two = middle_element - n // 2 + 1 - (ceil(n / 2) + 1)
        i = 1
        for _ in range(ceil(n / 2)):
            print(i, starting_number_one)
            i += 1
            starting_number_one += 1
        for _ in range(n // 2):
            print(i, starting_number_two)
            i += 1
            starting_number_two += 1