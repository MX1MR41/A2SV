# Solution 1
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # bfs
        # multi-source bfs from dominoes that got pushed 

        res = dict()

        que = deque()
        n = len(dominoes)
        seen = set()

        for i in range(n):
            if dominoes[i] == "L":
                que.append((i, -1))
            elif dominoes[i] == "R":
                que.append((i, 1))

        skip = set()
        
        while que:
            curr = dict()

            for _ in range(len(que)):
                i, d = que.popleft()
                if i in seen:
                    continue

                seen.add(i)
                res[i] = "L" if d == -1 else "R"

                if d == -1:

                    if (
                        i - 1 >= 0
                        and i - 1 not in res
                        and dominoes[i - 1] == "."
                        and i - 1 not in seen
                    ):
                        if i - 1 in curr and curr[i - 1] == 1:
                            skip.add(i - 1)
                            pass
                        else:
                            que.append((i - 1, -1))
                            curr[i - 1] = -1

                else:
                    if (
                        i + 1 < n
                        and i + 1 not in res
                        and dominoes[i + 1] == "."
                        and i + 1 not in seen
                    ):
                        if i + 1 in curr and curr[i + 1] == -1:
                            skip.add(i + 1)
                            pass

                        else:
                            que.append((i + 1, 1))
                            curr[i + 1] = 1

        final = ""
        for i in range(n):
            if i in skip or i not in res:
                final += "."
            else:
                final += res[i]

        return final


# Solution 2

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # dp
        # use two arrays, for right and left, to keep track of how long it will take
        # for a dominoe to fall to either the right or left due to by being pushed
        # either initially or by other dominoes

        n = len(dominoes)
        right = [-1] * n # -1 if this dominoe doesn't fall to the right
        last_right = -1 # most recent dominoe from the left that falls to the right
        for i in range(n):
            if dominoes[i] == "R":
                last_right = i # this node becomes the most recent dominoe to fall right
                right[i] = 0 # this node falls at time 0
                
            elif dominoes[i] == "L":
                last_right = -1
            else:
                if last_right != -1:
                    right[i] = i - last_right


        left = [-1] * n # -1 if this dominoe doesn't fall to the left
        last_left = -1 # most recent dominoe from the right that falls to the left
        for i in range(n - 1, -1, -1):
            if dominoes[i] == "L":
                last_left = i
                left[i] = 0
            elif dominoes[i] == "R":
                last_left = -1
            else:
                if last_left != -1:
                    left[i] = last_left - i



        res = ""

        for i in range(n):
            if right[i] == left[i]:
                res += "."

            elif right[i] != -1 and left[i] != -1:
                if right[i] < left[i]:
                    res += "R"
                else:
                    res += "L"

            elif right[i] == -1:
                res += "L"

            elif left[i] == -1:
                res += "R"
                
            else:
                res += "."

        return res

