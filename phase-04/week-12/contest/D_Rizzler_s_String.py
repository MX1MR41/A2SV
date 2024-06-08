"""
https://codeforces.com/gym/527294/problem/D

"""



mod = 10**9 + 7
s = input()

sequences = 0
before_last_b = 0 

for idx, char in enumerate(s):
    if char == 'b':
        before_last_b = sequences
    
    elif char == 'a':
        sequences += before_last_b + 1
        sequences %= mod

print(sequences)