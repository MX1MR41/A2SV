class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        ind = defaultdict(list)
        ans = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                ind[i+j].append(mat[i][j])

        ans.extend(ind.pop(0))

        i, rev = 1, 1 # rev is just a variable to determine whether to reverse

        while ind:
            if rev % 2:
                ans.extend(ind.pop(i))
            else:
                ans.extend(ind.pop(i)[::-1])

            i += 1
            rev += 1

        return ans

