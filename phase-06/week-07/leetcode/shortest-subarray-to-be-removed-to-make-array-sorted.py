class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # prefix sum + binary search
        # 1) we could remove a subarray that starts from 0
        # 2) remove a subarray that ends at n - 1
        # 3) remove a subarray that is in the middle i.e. doesn't reach either ends
        # For the first two cases we build a prefix and suffix to figure out the 
        # maximum valid subarray length we could get starting from either end.
        # For the third case we use binary search to find out the smallest length
        # we need to remove to make a valid array

        n = len(arr)

        # build prefix
        prefix = [True]
        pre = True
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                pre = False
            prefix.append(pre)

        # build suffix
        suffix = [True]
        suff = True
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                suff = False
            suffix.append(suff)
        suffix.reverse()

        # compute the maximum valid subarray length from either end
        max_left = max_right = 1
        ind = 1
        while ind < n and prefix[ind]:
            ind += 1
            max_left += 1

        ind = n - 2
        while ind >= 0 and suffix[ind]:
            ind -= 1
            max_right += 1

        # checks whether remove a subarray of length x from the middle of the array
        # gives us a valid array
        def check(x):
            if x + 1 >= n: # removing this much amount will leave a valid array
                return True

            l = 0
            for r in range(x + 1, n):
                # if the pre and suff are valid and arr[l] and arr[r] can be joined
                if prefix[l] and suffix[r] and arr[l] <= arr[r]:
                    return True
                l += 1

            return False


        ans = 0
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r)//2
            
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return min(ans, n - max_left, n - max_right)


            

        
