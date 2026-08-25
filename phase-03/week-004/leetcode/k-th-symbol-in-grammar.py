class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # this recursive generation of numbers has a pattern 
        # a given ith row will have its first half of numbers
        # the same as the (i-1)th row and 
        # its second half will be the complement of the (i-1)th row's 
        if n ==1 and k == 1:
            return 0
        mid = pow(2, n-1)//2

        res = 1
        if k <= mid:
            res = self.kthGrammar(n-1, k)
        else:
            res = 1 ^ self.kthGrammar(n-1,k-mid)

        return res