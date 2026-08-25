class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        def search(x):
            l, r = 0, len(banned) - 1

            while l <= r:
                mid = (l + r)//2
                if banned[mid] == x:
                    return True

                if banned[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1

            return banned[mid] == x

        count = 0
        currSum = 0


        for i in range(1, n+1):
            if not search(i) and currSum + i <= maxSum:
                count += 1
                currSum += i

        return count

            

        
