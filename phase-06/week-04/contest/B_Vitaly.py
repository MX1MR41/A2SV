n = int(input())
arr = list(map(int, input().split()))
arr.sort()
neg = sum([1 for i in arr if i < 0])

# print(neg)
s1, s2, s3 = [], [], []

# for i in arr

if neg % 2:
    s1.append(arr[0])
    for i in arr[1:]:
        if i > 0:
            s2.append(i)

        # elif i == 0:
        #     s3.append(i)

        else:
            s3.append(i)
# 
else:
    s1.append(arr[0])
    for i in arr[1:]:
        if i > 0:
            s2.append(i)

        else:
            s3.append(i)


if not s2:
    s2 = s3[:2]
    s3 = s3[2:]
print(len(s1), *s1)
print(len(s2), *s2)
print(len(s3), *s3)
