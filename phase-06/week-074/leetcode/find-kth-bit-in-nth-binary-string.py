# precompute sizes for each n iteration
size = [0] * (21)
size[1] = 1
for i in range(2, 21):
    size[i] = 2 * (size[i - 1]) + 1


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # recursion

        def solve(n, k):
            
            if n == 1:
                return "0"

            mid = n//2
            
            # mid is always 1
            if k == mid:
                return "1"

            # simulate where it would've been in the previous iteration as well as invert
            if k > mid:
                dist_from_mid = k - mid
                in_lower_half = mid - dist_from_mid
                

                return str(1 - int(solve(n//2, in_lower_half)))
            
            # simulate where it would've been in the prev iteration but do no invert
            else:
                return str(int(solve(n//2, k)))

        
        n = size[n]
        return solve(n, k - 1)
