# BACKTRACKING FINAL BOSS
# first generate and store all possible permutation of numbers and operations
# then evaluate each one by all possible permutation of order of operations,
# that way simulating all possible placements of paranthesis
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = set(["+", "-", "*", "/"])

        choices = []

        def dfs(ind, used, curr):
            if ind == len(cards):
                choices.append(curr[:-1])
                return

            for i in range(len(cards)):
                if not used & (1 << i):
                    new_used = used | (1 << i)
                    for op in ops:
                        dfs(ind + 1, new_used, curr + [cards[i], op])

        dfs(0, 0, [])

        for choice in choices:

            if self.evaluate(choice):
                return True

        return False

    def evaluate(self, arr):
        ops = set(["+", "-", "*", "/"])

        def dfs(curr):

            if len(curr) == 1:
                return abs(curr[0] - 24) <= 10 ** (-5)

            for i in range(len(curr)):
                if curr[i] in ops:
                    a = curr[i - 1]
                    b = curr[i + 1]
                    if curr[i] == "+":
                        c = a + b
                    elif curr[i] == "-":
                        c = a - b
                    elif curr[i] == "*":
                        c = a * b
                    else:
                        if b == 0:
                            continue

                        c = a / b

                    new_curr = curr[: i - 1] + [c] + curr[i + 2 :]
                    if dfs(new_curr):
                        return True

            return False

        return dfs(arr)
