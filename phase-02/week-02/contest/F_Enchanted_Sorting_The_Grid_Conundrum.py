"""

https://codeforces.com/gym/495129/problem/F
"""

t = int(input())
for _ in range(t):
    
    grid = []
    n, m = map(int, input().split())
    
    for row in range(n):
        grid.append(list(map(int, input().split())))


    unsorted_row = None
    # check if every row is sorted
    for row in range(n):
        for col in range(1, m):
            if grid[row][col - 1] > grid[row][col]:
                unsorted_row = grid[row]
                break
        
        if unsorted_row != None:
            break
    
    # if all rows are already sorted we can swap the first column with itself as an answer
    if unsorted_row == None:
        print(1, 1)
        continue
    

    sorted_version = sorted(unsorted_row)
    disordered_columns = []
    can_be_good = True

    # identify the indices whose values are not in their sorted positions in the unsorted row
    for indx in range(m):
        if unsorted_row[indx] != sorted_version[indx]:
            disordered_columns.append(indx)

            if len(disordered_columns) >= 3:
                can_be_good = False
                break
        
    # if those indices are more than 3, we can't make it sorted with a single swap
    if not can_be_good:
        print(-1)
        continue

    # swap the corresponding columns of those indices
    for row in range(n):
        col1, col2 = disordered_columns
        grid[row][col1], grid[row][col2] = grid[row][col2], grid[row][col1]

    # check if all rows are sorted after the swap
    for row in range(n):
        for col in range(1, m):
            if grid[row][col - 1] > grid[row][col]:
                can_be_good = False
                break
        
        if not can_be_good:
            break
    
    if not can_be_good:
        print(-1)
    
    else:
        print(disordered_columns[0] + 1, disordered_columns[1] + 1)