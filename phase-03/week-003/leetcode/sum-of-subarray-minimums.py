class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        nxt, prev = [-1] * n, [-1] * n
        stack = []

        # Finding the next smaller element for each element to the right
        for i, x in enumerate(arr):
            while stack and arr[stack[-1]] > x:
                j = stack.pop()
                nxt[j] = i
            stack.append(i)

        stack.clear()

        # Finding the next smaller element for each element to the left
        for i, x in reversed(list(enumerate(arr))):
            while stack and arr[stack[-1]] >= x:
                j = stack.pop()
                prev[j] = i
            stack.append(i)

        res = 0
        for i in range(n):
            # Length of subarrays where arr[i] is the minimum
            left_length = i - prev[i] if prev[i] != -1 else i + 1
            right_length = nxt[i] - i if nxt[i] != -1 else n - i
            res += arr[i] * left_length * right_length

        return res % MOD
