class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] != 1:
            arr[0] = 1
        ans = 1
        n = len(arr)

        for i in range(n-1):
            a , b = arr[i], arr[i+1]

            if abs(a-b) > 1:
                arr[i+1] = a + 1
            ans = max(ans, arr[i+1])

        return ans



        
        