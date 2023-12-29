class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans, d = "", defaultdict(list) 
        # dictionary to hold str form of nums each mapped to the leftmost digit

        for i in range(len(nums)):
            d[str(nums[i])[0]].append(str(nums[i]))

        for j in d:
            l = d[j]
            #bubble sort to get the combination of nums that give the largest integer
            for i in range(len(l)-1):
                for j in range(i, len(l)):
                    s1 = "".join(l) # without swapping
                    l[i], l[j]= l[j], l[i]
                    s2 = "".join(l) # after swapping
                    if s2 < s1:
                        l[i], l[j]= l[j], l[i]

        dkeys = sorted(d.keys(), reverse = True)

        for i in dkeys:
            ans += "".join(d[i])

        #handling edgecase of repeating zeros like "00"
        zeros, found = "", False
        for i in range(len(ans) - 1): 
#1st condition handles "100, 200", then check for consecutive zeros with no other dig in front
            if ans[0] == '0' and ans[i] == '0' and ans[i+1] == '0':
                found = True
                j = i+1
                while j < len(ans)-1 and ans[j] == "0":
                    j += 1
                zeros = '0' * (j-i+1)
                break

        if found:
            ans = ans.replace(zeros, "0")

        return ans
            
        