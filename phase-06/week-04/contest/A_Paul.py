from collections import defaultdict


for _ in range(int(input())):
    s = input()
    valid = []
    count = defaultdict(int)

    for i in s:
        if count[i] <= 1:
            valid.append(i)

        count[i] += 1

    # print(valid, len(valid), len(valid)//2)
    print(len(valid)//2)
