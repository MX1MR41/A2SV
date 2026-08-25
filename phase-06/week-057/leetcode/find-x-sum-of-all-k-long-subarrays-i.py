class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # sliding window + heap + lazy deletion
        res = []
        heap = []
        freq = Counter()

        for i in range(k):
            freq[nums[i]] += 1

        for num, f in freq.items():
            heappush(heap, (-f, -num))

        temp = []
        summ = 0
        while heap and len(temp) < x:
            f, num = heappop(heap)
            temp.append((f, num))
            summ += f * num

        res.append(summ)
        summ = 0
        for item in temp:
            heappush(heap, item)

        

        l = 0
        for r in range(k, len(nums)):
            freq[nums[l]] -= 1
            freq[nums[r]] += 1

            heappush(heap, (-freq[nums[r]], -nums[r]))
            heappush(heap, (-freq[nums[l]], -nums[l]))

            temp = []
            summ = 0
            seen = set()
            while heap and len(temp) < x:
                f, num = heappop(heap)
                if freq[-num] != -f or num in seen:
                    continue
                
                # print((f, num))
                seen.add(num)
                temp.append((f, num))
                summ += f * num

            # print(temp)
            for item in temp:
                heappush(heap, item)
            # print("heap = ", heap)
            # print("="*20)

            res.append(summ)



            l += 1

        return res
