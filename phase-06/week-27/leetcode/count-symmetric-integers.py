class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            stri = str(i)
            if not len(stri) % 2:
                n = len(stri)
                if sum(map(int, stri[:n//2])) == sum(map(int, stri[n//2:])):
                    count += 1

        return count
        
