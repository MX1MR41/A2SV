class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        A = [nums1[i] - nums2[i] for i in range(len(nums1))]
        ans = [0]

        def mergeSort(A, l, r, diff, ans):
            if l >= r:
                return

            m = (l + r) // 2
            mergeSort(A, l, m, diff, ans)
            mergeSort(A, m + 1, r, diff, ans)
            merge(A, l, m, r, diff, ans)

        def merge(A, l, m, r, diff, ans):
            lo = m + 1
            hi = m + 1 

            for i in range(l, m + 1):
                while hi <= r and A[i] > A[hi] + diff:
                    hi += 1
                ans[0] += r - hi + 1

            sorted_arr = [0] * (r - l + 1)
            k = 0  
            i = l  
            j = m + 1  

            while i <= m and j <= r:
                if A[i] < A[j]:
                    sorted_arr[k] = A[i]
                    i += 1
                else:
                    sorted_arr[k] = A[j]
                    j += 1
                k += 1

            while i <= m:
                sorted_arr[k] = A[i]
                i += 1
                k += 1

            while j <= r:
                sorted_arr[k] = A[j]
                j += 1
                k += 1

            A[l:r + 1] = sorted_arr

        mergeSort(A, 0, len(A) - 1, diff, ans)
        return ans[0]

