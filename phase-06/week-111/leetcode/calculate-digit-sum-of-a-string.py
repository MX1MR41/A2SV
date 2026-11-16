class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = list(map(int, s))
            new_s = []
            c = 0
            for i in range(len(s)):
                if c == k:
                    new_s.append(s[i])

                    c = 1

                else:
                    if new_s == []:
                        new_s.append(s[i])
                    else:
                        new_s[-1] += s[i]

                    c += 1

            s = "".join(map(str, new_s))

        return s
