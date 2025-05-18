# Solution 1
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # dp
        # enumerate all possible patterns that a single column can be colored in using backtracking
        # color the grid column by column, using the possible color patterns of a single column
        # based on what the previous column was colored in

        patterns = set()

        def can_be_side_by_side(pat1, pat2):
            for i in range(m):
                if pat1[i] == pat2[i]:
                    return False

            return True

        # function to backtrack and enumerate all possible patterns that a single column can have
        def dfs(pat, i):
            nonlocal patterns

            if i == m:
                patterns.add(pat)
                return 

            list_pat = list(pat)
            prev = list_pat[-1]

            for color in [1, 2, 3]:

                if color != prev:
                    new_list_pat = list_pat + [color]
                    new_pat = tuple(new_list_pat)

                    dfs(new_pat, i + 1)


        # backtrack with the first cell colored as red(1), blue(2) and green(3)
        dfs((1,), 1)
        dfs((2,), 1)
        dfs((3,), 1)


        patterns = [list(pat) for pat in patterns]
        len_patterns = len(patterns)

        # side_by_side[i][j] = True is patterns[j] can be next to patterns[i]
        side_by_side = [[False for _ in range(len_patterns)] for _ in range(len_patterns)]

        for i in range(len_patterns):
            pat1 = patterns[i]
            for j in range(len_patterns):
                if i == j:
                    continue

                pat2 = patterns[j]

                if can_be_side_by_side(pat1, pat2):
                    side_by_side[i][j] = True


        # prev_column[pattern] = [whether_column_can_be_colored_in_this_pattern, number_of_ways]
        # initially, the first column can be colored in any pattern, in a single way each
        prev_column = [[True, 1] for _ in range(len_patterns)]

        for i in range(1, n):
            # initially, no pattern can be used to color current column
            curr_column = [[False, 0] for _ in range(len_patterns)]

            for p1 in range(len_patterns):
                if prev_column[p1][0] == False: # this pattern wasn't used in previous column, skip
                    continue

                for p2 in range(len_patterns):
                    if side_by_side[p1][p2]: # if p2 can be put beside p1
                        curr_column[p2][0] = True # p2 can be used as a coloring pattern for column
                        curr_column[p2][1] += prev_column[p1][1] # add number of ways of p1 to p2


            prev_column = deepcopy(curr_column)

        MOD = 10**9 + 7
        res = 0

        for i in range(len_patterns):
            res = (res + prev_column[i][1]) % MOD


        return res 




# Solution 2

class Solution:
    def multiply(self, matA, matB):
        """
        Given two matrices matA and matB where num of cols of matA == num of rows in matB,
        this function performs matrix multiplication matA x matB and returns the result
        """

        rows = len(matA)
        cols = len(matB[0])

        res = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            row = matA[r]
            for c in range(cols):
                col = [matB[i][c] for i in range(cols)]

                cell = 0
                for i in range(cols):
                    cell = (cell + row[i] * col[i]) % self.MOD

                res[r][c] = cell

        return res

    def power(self, mat, exponent):
        """
        Given a matrix mat and an integer exponent, this function computes the result of raising
        mat to the power of exponent. It does this in a binary exponentiation method
        """

        if exponent == 1:
            return mat

        half = self.power(mat, exponent // 2)

        res = self.multiply(half, half)

        if exponent % 2 == 1:
            res = self.multiply(mat, res)

        return res


    def colorTheGrid(self, m: int, n: int) -> int:
        # dp + matrix exponentiation
        # since we are going to transform a vector multiple times using the same rules,
        # we can use matrix exponentiation. The transformation rules will be represented in a matrix
        # where matrix[i][j] == 1 if patterns[j] can be put side by side with patterns[i]
        # then, we raise the matrix to the power of n - 1 (the number of columns except the first)
        # because we apply the transformation that number of times. We use binary exponentiation for
        # logarithmic exponentiation.


        self.MOD = 10**9 + 7

        patterns = set()

        def can_be_side_by_side(pat1, pat2):
            for i in range(m):
                if pat1[i] == pat2[i]:
                    return False

            return True

        # function to backtrack and enumerate all possible patterns that a single column can have
        def dfs(pat, i):
            nonlocal patterns

            if i == m:
                patterns.add(pat)
                return 

            list_pat = list(pat)
            prev = list_pat[-1]

            for color in [1, 2, 3]:

                if color != prev:
                    new_list_pat = list_pat + [color]
                    new_pat = tuple(new_list_pat)

                    dfs(new_pat, i + 1)


        # backtrack with the first cell colored as red(1), blue(2) and green(3)
        dfs((1,), 1)
        dfs((2,), 1)
        dfs((3,), 1)


        patterns = [list(pat) for pat in patterns]
        len_patterns = len(patterns)

        # matrix[i][j] = True is patterns[j] can be next to patterns[i]
        matrix = [[0 for _ in range(len_patterns)] for _ in range(len_patterns)]

        for i in range(len_patterns):
            pat1 = patterns[i]
            for j in range(len_patterns):
                if i == j:
                    continue

                pat2 = patterns[j]

                if can_be_side_by_side(pat1, pat2):
                    matrix[i][j] = True


        if n == 1:
            return len_patterns % self.MOD


        powered_matrix = self.power(matrix, n - 1)

        initial = [[1 for _ in range(len_patterns)]]

        res = self.multiply(initial, powered_matrix)

        tot = 0
        for i in res[0]:
            tot = (tot + i) % self.MOD

        return tot
        
            

            
        
