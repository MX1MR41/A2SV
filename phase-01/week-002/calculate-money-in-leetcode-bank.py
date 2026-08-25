class Solution:
    def totalMoney(self, n: int) -> int:
        days, i = [], 1

        for j in range(1, n+1):
            days.append(i)
            i += 1

            if j % 7 == 0:
                i = (j // 7) + 1

        return sum(days)
