class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = [0 for _ in range(10)]
        for i in digits:
            cnt[i] += 1

        total = 0
        for i in range(100, 1000):
            a = i // 100
            b = (i % 100) // 10
            c = i % 10
            if c % 2:
                continue

            if a == b == c:
                if cnt[a] >= 3:
                    total += 1
            elif (a == b):
                if cnt[a] >= 2 and cnt[c] >= 1:
                    total += 1
            elif (a == c):
                if cnt[a] >= 2 and cnt[b] >= 1:
                    total += 1
            elif (b == c):
                if cnt[b] >= 2 and cnt[a] >= 1:
                    total += 1
            else:
                if cnt[a] >= 1 and cnt[b] >= 1 and cnt[c] >= 1:
                    total += 1


        return total


        
