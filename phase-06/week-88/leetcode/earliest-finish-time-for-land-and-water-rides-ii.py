class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # prefix/suffix sum (prefix and suffix min actually)
        res = float("inf")

        land = list(zip(landStartTime, landDuration))
        land.sort()

        water = list(zip(waterStartTime, waterDuration))
        water.sort()

        max_end = max(max(l[0] + l[1] for l in land), max(w[0] + w[1] for w in water))

        min_started = [float("inf")] * (max_end + 1)
        min_to_start = [float("inf")] * (max_end + 1)

        ind = 0

        for i in range(max_end + 1):
            while ind < len(water) and water[ind][0] <= i:
                min_started[i] = min(min_started[i], water[ind][1])

                ind += 1

            if i > 0:
                min_started[i] = min(min_started[i], min_started[i - 1])

        ind = len(water) - 1
        for i in range(max_end, -1, -1):
            while ind >= 0 and water[ind][0] >= i:
                min_to_start[i] = min(min_to_start[i], water[ind][1])
                ind -= 1

            if i < max_end:
                min_to_start[i] = min(min_to_start[i], min_to_start[i + 1] + 1)
    


        for l in land:
            l_end = l[0] + l[1]

            w_min = min(min_started[l_end], min_to_start[l_end])

            curr = l_end + w_min

            res = min(res, curr)

        min_started = [float("inf")] * (max_end + 1)
        min_to_start = [float("inf")] * (max_end + 1)

        ind = 0

        for i in range(max_end + 1):
            while ind < len(land) and land[ind][0] <= i:
                min_started[i] = min(min_started[i], land[ind][1])

                ind += 1

            if i > 0:
                min_started[i] = min(min_started[i], min_started[i - 1])

        ind = len(land) - 1
        for i in range(max_end, -1, -1):
            while ind >= 0 and land[ind][0] >= i:
                min_to_start[i] = min(min_to_start[i], land[ind][1])
                ind -= 1

            if i < max_end:
                min_to_start[i] = min(min_to_start[i], min_to_start[i + 1] + 1)
    


        for w in water:
            w_end = w[0] + w[1]

            l_min = min(min_started[w_end], min_to_start[w_end])

            curr = w_end + l_min

            res = min(res, curr)

        return res


