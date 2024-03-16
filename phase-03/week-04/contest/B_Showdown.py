"""

https://codeforces.com/gym/508328/problem/B

PASSED
"""

def f(curr_round, score_A, score_B, rem_A, rem_B):
    if curr_round > 10:
        return 0
    
    if score_A > score_B + rem_B:
        return 0
    
    if score_B > score_A +rem_A:
        return 0
    
    if curr_round % 2:
        if s[curr_round - 1].isdigit():
            result = s[curr_round - 1] == "1"
            return 1 + f(curr_round + 1, score_A + result, score_B, rem_A - 1, rem_B)
        
        else:
            goal = 1 + f(curr_round + 1, score_A + 1, score_B, rem_A - 1, rem_B)
            no_goal = 1 + f(curr_round + 1, score_A, score_B, rem_A -1, rem_B)

            return min(goal, no_goal)
    else:
        if s[curr_round - 1].isdigit():
            result = s[curr_round - 1] == "1"
            return 1 + f(curr_round + 1, score_A , score_B + result, rem_A , rem_B- 1)
        
        else:
            goal = 1 + f(curr_round + 1, score_A , score_B+ 1, rem_A, rem_B - 1)
            no_goal = 1 + f(curr_round + 1, score_A, score_B, rem_A , rem_B -1)

            return min(goal, no_goal)


for _ in range(int(input())):
    s = input()
    print(f(1,0,0,5,5))

    