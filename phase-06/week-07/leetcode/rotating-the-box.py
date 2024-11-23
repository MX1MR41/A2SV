class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # first move every stone until it meets an obstacle or edge
        # then rotate the box by first transposing it then flipping it sideways
        m, n = len(box), len(box[0])

        for mat in box:
            for i in range(n - 2, -1, -1):
                if mat[i] == "#":
                    while i + 1 < n and mat[i + 1] == ".":
                        mat[i], mat[i + 1] = mat[i + 1], mat[i]
                        i += 1


        transpose = [[""] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                transpose[j][i] = box[i][j]

        for row in transpose:
            row.reverse()

        return transpose
        
