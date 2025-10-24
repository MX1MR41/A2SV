class Solution:
    def isBeautiful(self, num):
        count = Counter(num)
        for i in count:
            if count[i] != int(i):
                return False

        return True

    def nextBeautifulNumber(self, n: int) -> int:
        # the maximum possible value for n is 10^6
        # and the answer for 10^6 would be the 1,224,444
        # so we can just traverse starting from n + 1 and return the first beautiful num
        for i in range(n + 1, 1224445):
            if self.isBeautiful(str(i)):
                return i


            
        
        
