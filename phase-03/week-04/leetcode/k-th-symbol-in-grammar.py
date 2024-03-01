class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # this recursive generation of numbers has a pattern 
        # a given ith row will have its first half of numbers
        # the same as the (i-1)th row and 
        # its second half will be the complement of the (i-1)th row's 
        
        def gram(n, k):
            if n == 1:
                return 0
            
            mid = 2 ** (n - 2)

            if k <= mid:
                return gram(n - 1, k)
                
            else:
                return 1 - gram(n - 1, k - mid)

        return gram(n, k)
