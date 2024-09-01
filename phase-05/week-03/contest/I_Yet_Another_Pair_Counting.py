import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

def conquer(l1, r1, l2, r2):

    excess_opening = defaultdict(int)
    inverted_open = 0
    unpaired_closing = 0
    # all closing brackets must have an opening pair on the left subarray
    # invert some suffix of substring 1
    for indx in range(r1, l1 - 1, -1):
        if s[indx] == ')':
            inverted_open += 1
            # follow kadan's algorithm to find opening matches for the closings
            # if we have an excess opening, it is no use for a closing that comes before it
            # so we don't make the unpaired_closing negative
            unpaired_closing = max(unpaired_closing - 1, 0) 
            
        else:
            unpaired_closing += 1
            inverted_open -= 1
        
        # uninverted prefix of this index must provide opening pairs for the unpaired closings
        if pref[indx - 1] >= unpaired_closing:
            excess_opening[pref[indx - 1] + inverted_open] += 1


    unpaired_opening = 0
    inverted_close = 0
    count = 0 # (l, r) matches 

    # invert some prefix of substring 2
    for indx in range(l2, r2 + 1):
        if s[indx] == '(':
            inverted_close += 1
            unpaired_opening = max(unpaired_opening - 1, 0)

        else:
            unpaired_opening += 1
            inverted_close -= 1

        # uninverted suffix of this index must provide closing pairs for the unpaired openings
        if suf[indx + 1] >= unpaired_opening:
            # match 'y' amount of excess opening in the first substring
            # with 'y' amount of closing in the second substring
            count += excess_opening[suf[indx + 1] + inverted_close]

    return count

def divide(l, r):
    if l >= r:
        return 0

    mid = (r + l)//2
    left_count = divide(l, mid)
    right_count = divide(mid + 1, r)
    cur_count = conquer(l, mid, mid + 1, r)
    return left_count + right_count + cur_count

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)

    pref = [0]*(n + 1)
    suf = [0]*(n + 1)

    openning_pref = 0
    closing_suf = 0
    for i in range(n):
        openning_pref += 1 if s[i] == '(' else -1
        closing_suf += 1 if s[n - i - 1] == ')' else -1

        pref[i] = openning_pref
        suf[n - i - 1] = closing_suf
    
    ans = divide(0, n - 1)
    print(ans)