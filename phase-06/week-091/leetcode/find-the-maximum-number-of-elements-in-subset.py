class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        cnt = Counter(nums)
        one = cnt[1]
        if not one % 2:
            one -= 1

        res = max(1, one)

        for num in nums:
            if num == 1:
                continue

            p = 1

            curr = 0
            while True:
                need = num ** p
                if cnt[need] >= 2:
                    curr += 2
                    p *= 2
                elif cnt[need] == 1:
                    curr += 1
                    res = max(res, curr)
                    break
                else:
                    curr -= 1
                    res = max(res, curr)
                    break

            # print(num, curr)

        return res

        
