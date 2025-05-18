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


            

            
        
