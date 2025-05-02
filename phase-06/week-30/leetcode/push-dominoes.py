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
