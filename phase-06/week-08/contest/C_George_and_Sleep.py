"""

PASSED

"""

s = input()
t = input()

tots = int(s[:2]) * 60 + int(s[3:])
tott = int(t[:2]) * 60 + int(t[3:])

# print(tots, tott)

if tott > tots:
    total = 24*60
    total -= (tott - tots)
    hours = str(total//60)
    mins = str(total % 60)
    if len(hours) == 1:
        hours = "0" + hours
    if len(mins) == 1:
        mins = "0" + mins

    print(hours + ":" + mins)
    exit()

total = tots - tott
hours = str(total//60)
mins = str(total % 60)
if len(hours) == 1:
    hours = "0" + hours
if len(mins) == 1:
    mins = "0" + mins

print(hours + ":" + mins)
exit()


