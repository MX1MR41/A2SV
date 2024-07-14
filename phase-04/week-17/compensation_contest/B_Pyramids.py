def f(x):
    return ((x)*(x+1))/2
cubes = int(input())
curr = 1
height = 1

while curr <= cubes:
    new = curr + f(height + 1)
    if new <= cubes:
        height += 1
        curr = new
    else:
        break

print(height)

    