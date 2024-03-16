"""

https://codeforces.com/gym/503628/problem/F

PASSED

"""

n = int(input())
a = list(map(int, input().split()))

pos_prefixes = 1 # as an identity, to take into account a whole prefix
neg_prefixes = 0

pos_seg_count = 0
neg_seg_count = 0

prefix = 1

for num in a:
    prefix *= (num//abs(num)) # we only want the sign, not the magnitude

    if prefix > 0:
        pos_seg_count += pos_prefixes
        neg_seg_count += neg_prefixes
        pos_prefixes += 1
        
    else:
        pos_seg_count += neg_prefixes
        neg_seg_count += pos_prefixes
        neg_prefixes += 1

print(neg_seg_count, pos_seg_count)