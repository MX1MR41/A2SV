s = input()
t, u = [], []

for i in s:
    if not t:
        t.append(i)
        continue

    if t and ord(i) < ord(t[-1]):
        while t and ord(i) < ord(t[-1]):
            u.append(t.pop())
        t.append(i)
    elif t and ord(i) > ord(t[-1]):
       
        t.append(i)


print("".join(t + u))