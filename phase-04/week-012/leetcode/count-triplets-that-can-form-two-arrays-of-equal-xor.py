class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        prefix = [0] * (N + 1)
        for i in range(N):

            prefix[i + 1] = prefix[i] ^ arr[i]

        ans = 0
        for i in range(N - 1):

            for j in range(i + 1, N):
    
                for k in range(j, N):
        
                    a = prefix[j] ^ prefix[i]
        
                    b = prefix[k + 1] ^ prefix[j]
        
                    if a == b:
                        ans += 1
        return ans
