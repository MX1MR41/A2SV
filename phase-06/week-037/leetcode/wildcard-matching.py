class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top-down dp (memoized DFS) to handle wildcard pattern matching
        # '?' matches any single character
        # '*' matches any sequence of characters (including empty)

        dp = {}  
        lens, lenp = len(s), len(p)

        def match(i: int, j: int) -> bool:
            # if result already computed, avoid recomputation
            if (i, j) in dp:
                return dp[(i, j)]

            # both string and pattern are fully consumed -> successful match
            if i >= lens and j >= lenp:
                return True


            # pattern exhausted but string remains -> no match
            if i < lens and j >= lenp:
                return False

            # string exhausted but pattern remains
            if i >= lens and j < lenp:
                # remaining pattern must all be '*' to match empty suffix
                if p[j] == '*':
                    # skip this '*' and try to match rest
                    return match(i, j + 1)
                else:
                    return False

            can = False  # flag indicating if s[i:] matches p[j:]
            
            if p[j] == '?':
                # '?' consumes exactly one character
                can = match(i + 1, j + 1)

            elif p[j] == '*':
                # '*' can match zero characters: move pattern forward
                # or match one char and stay on '*', or match one char and move on
                # zero-length: skip '*' in pattern
                if match(i, j + 1):
                    can = True
                # consume one char but stay on '*'
                elif match(i + 1, j):
                    can = True
                # consume one char and move past '*'
                elif match(i + 1, j + 1):
                    can = True

            else:
                # literal character: must match exactly
                if s[i] == p[j]:
                    can = match(i + 1, j + 1)

            # store and return result
            dp[(i, j)] = can
            return can

        return match(0, 0)
