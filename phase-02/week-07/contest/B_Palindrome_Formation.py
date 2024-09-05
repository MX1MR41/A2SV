for _ in range(int(input())):
    n = int(input())
    s = input()
    i, j = 0, n - 1
    left = right = 0
    templeft, tempright = [], []
    flag = False
    while i < j:
        if s[i] != s[j]:
            if not left and not right and templeft and tempright:
                flag = True
                break
            else:
                left += 1
                right += 1
        else:
            if left and right:
                templeft.append(left)
                tempright.append(right)
            left = right = 0

        i += 1
        j -= 1

    if flag: print("No")
    else:
        if right == left:
            print("Yes")
        else:
            print("No")

