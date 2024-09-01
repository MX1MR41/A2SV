"""

PASSED

"""

from collections import defaultdict

for _ in range(int(input())):
    a, b = input().split()

    if a == b:
        print("YES")
        continue

    inds = defaultdict(list)

    for ind, letter in enumerate(a):
        inds[letter].append(ind)

    b = list(b)
    # a = list(a)

    last_ind = float("inf")
    n = len(b)
    for _ in range(n):
        curr_b = b[-1]
        if not inds[curr_b]:
            # print("first break")
            break

        curr_ind = inds[curr_b].pop()
        # print("currently ", curr_b, curr_ind, last_ind)
        if curr_ind >= last_ind:
            # print("second break")
            break
        
        last_ind = curr_ind
        b.pop()

    if not b:
        print("YES")
    else:
        print("NO")

        


    # print(inds)
    # print("\n\n")