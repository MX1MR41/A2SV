class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # prefix sum
        # since the numbers are so large, we can't use an array. Instead we use
        # a hashmap to store only the impprtant indices and compute over them
        pre = defaultdict(int)

        for l, r in meetings:

            pre[l] += 1
            pre[r + 1] -= 1

        arr = sorted([[i, j] for i, j in pre.items()])

        for i in range(1, len(arr)):
            arr[i][1] += arr[i - 1][1]
        

        if arr[0][0] != 1:
            arr = [[1, 0]] + arr

        if arr[-1][0] < days:
            arr.append([days, 0])
        
        

        ind = 0
        res = 0

        while ind < len(arr) and arr[ind][0] <= days:
            if arr[ind][1] == 0:
                if ind < len(arr) - 1:
                    res += arr[ind + 1][0] - arr[ind][0]
                else:
                    res += 1

            ind += 1

        return res 


        # for i in range(1, days):
        #     pre[i] += pre[i - 1]
        
        
        # return pre.count(0)
        
