class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[-1]

        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l+r)//2

            if letters[mid] <= target:
                l = mid + 1

            else:
                r = mid - 1
                res = letters[mid]

        return res if res > target else letters[0]
        