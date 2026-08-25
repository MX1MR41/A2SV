class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        rows = len(strs)
        cols = len(strs[0])

        sorted_pairs = [False] * (rows - 1)

        deletions = 0

        for c in range(cols):

            conflict_found = False

            for i in range(rows - 1):

                if not sorted_pairs[i]:

                    letter_top = strs[i][c]
                    letter_bottom = strs[i + 1][c]

                    if letter_top > letter_bottom:

                        conflict_found = True
                        break

            if conflict_found:
                deletions += 1

            else:

                for i in range(rows - 1):

                    if not sorted_pairs[i]:
                        letter_top = strs[i][c]
                        letter_bottom = strs[i + 1][c]

                        if letter_top < letter_bottom:
                            sorted_pairs[i] = True

        return deletions
