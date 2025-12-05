class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # sorting + binary search
        # start from the largest batteries and whenever you need more charge
        # take from the smallest batteries at the end of the reverse sorted array
        batteries.sort(reverse = True)


        def check(time):
            temp = batteries[:]
            last_ind = len(temp) - 1
            for i in range(n):
                while temp[i] < time and last_ind > i:
                    add = min(time - temp[i], temp[last_ind])
                    temp[i] += add
                    temp[last_ind] -= add
                    if temp[last_ind] == 0:
                        last_ind -= 1


                if temp[i] < time or last_ind < n - 1:
                    return False

            return True


        res = 0
        l, r = 0, sum(batteries)

        while l <= r:
            mid = (l + r)//2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res

        
