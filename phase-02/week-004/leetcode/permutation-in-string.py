class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n2 < n1:
            return False

        cnt_s1 = Counter(s1)
        cnt_s2 = Counter(s2[:n1])

        if cnt_s2 == cnt_s1:
                return True

        for i in range(1, n2- n1 + 1):
            last = s2[i - 1]
            new = s2[i + n1 -1]

            cnt_s2[last] -= 1
            if cnt_s2[last] == 0:
                cnt_s2.pop(last)

            cnt_s2[new] += 1

            if cnt_s2 == cnt_s1:
                return True

        return False

        