class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        ixn = set(cnt1.keys()).intersection(set(cnt2.keys()))
        print(ixn)

        ans = []

        for i in ixn:
            for _ in range(min(cnt1[i], cnt2[i])):
                ans.append(i)

        return ans
        