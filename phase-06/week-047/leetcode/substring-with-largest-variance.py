class Solution:
    def largestVariance(self, s: str) -> int:
        # prefix sum + kadane algorithm
        # solve for every possible pairwise combination of all letters
        # to solve for two letters a and b, assign +1 to a and -1 to b in an array
        # iterate over the array and essentially find the maximum sum subarray,
        # if the maximum sum subarray happens to have no b's in it, the result could be
        # maximum sum subarray - 1 to include one occurence of letter b. 

        def versus(a, b):
            res = 0
            arr = []
            for i in s:
                if i == chr(a):
                    arr.append(1)
                elif i == chr(b):
                    arr.append(-1)

            max_consecutive = 0
            summ = 0
            l = 0
            for r in range(len(arr)):

                summ += arr[r]

                if summ < 0:
                    summ = 0
                    l = r + 1

                    continue

                if summ == r - l + 1:
                    max_consecutive = max(max_consecutive, summ)
                else:
                    res = max(res, summ)

            if len(arr) > max_consecutive:
                res = max(res, max_consecutive - 1)

            return res

        res = 0

        for a in range(97, 123):
            for b in range(97, 123):
                if a == b:
                    continue

                curr = versus(a, b)

                res = max(res, curr)

        return res
