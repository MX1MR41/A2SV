class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        nevens = n//2
        nodds = n - nevens
        
        mevens = m//2
        modds = m - mevens

        res = modds * nevens + mevens * nodds


        return res
        
