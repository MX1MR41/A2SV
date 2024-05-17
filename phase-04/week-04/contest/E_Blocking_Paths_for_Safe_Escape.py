"""

https://codeforces.com/gym/515998/problem/E


"""

def inBound(row, col, n, m, visited, graph):
    return 0 <= row < n and 0 <= col < m and (row, col) not in visited and graph[row][col] != '#'

def main():
     for _ in range(int(input())):
        n, m = map(int, input().split())
        graph = []

        for _ in range(n):
            graph.append(list(input()))
        
        direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        good, bad, empty = [], [], []

        # Find the good, bad and empty cells
        for row in range(n):
            for col in range(m):
                if graph[row][col] == 'G':
                    good.append((row, col))
                elif graph[row][col] == 'B':
                    bad.append((row, col))
                elif graph[row][col] == '.':
                    empty.append((row, col))

        # Replace the empty cells with walls if they are adjacent to bad cells
        for row, col in empty:
            for i, j in direc:
                _row, _col = row + i, col + j
                if 0 <= _row < n and 0 <= _col < m and graph[_row][_col] == 'B':
                    graph[row][col] = '#'
                    break 

        # Check if the good cells are reachable and the bad cells are not reachable
        stack = [(n - 1, m - 1)]
        visited = set()
        while stack:
            row, col = stack.pop()
            if not inBound(row, col, n, m, visited, graph):
                continue
            visited.add((row, col))
            for i, j in direc:
                _row, _col = row + i, col + j
                stack.append((_row, _col))

        ans = 'Yes'
        for cell in good:
            if cell not in visited:
                ans = 'No'
                break
        
        for cell in bad:
            if cell in visited:
                ans = 'No'
                break

        print(ans)

if __name__ == '__main__':
    main()