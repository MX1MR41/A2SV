class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # greedy + sorting
        # let's say nums[i]^k being greater than nums[i] as an "inversion"
        # if we have two inversions, we can keep xoring them with their neighbours by inverting,
        # and kind moving the inversion so that they are side-by-side, 
        # then we can invert both at the the same time, effectively cancelling eacg other out.
        # Once we gather such inversions, we can keep inverting them two-by-two until we are left 
        # with either none or one inversion.
        # For that one inversion, we try to find a "clean" (nums[i] >= nums[i]^k) node, and if 
        # inverting the clean node with the clean node causes an increase in the total sum,
        # we sacrifice the clean node and invert it.

        n = len(nums)
        num_and_xor = [(nums[i], nums[i] ^ k, i) for i in range(n)]
        inversions = []
        inv_count = 0

        clean = []

        for num, xor, ind in num_and_xor:
            if xor > num:
                inversions.append((num, xor, ind))
                inv_count += 1
            else:
                clean.append((num, xor, ind))

        inversions.sort(key=lambda x: x[1] - x[0])
        clean.sort(key=lambda x: x[1] - x[0])


        # cancel out inversions two-by tow, i.e. xor them
        while len(inversions) >= 2:

            num, xor, ind = inversions.pop()
            nums[ind] = xor

            num, xor, ind = inversions.pop()
            nums[ind] = xor

        # prune the end of the clean array of nodes whose xoring will cause a net decrease in sum
        while (
            inversions
            and clean
            and  (inversions[-1][1] - inversions[-1][0]) + (clean[-1][1] - clean[-1][0]) <= 0 
        ):

            clean.pop()


        if inversions:
            num, xor, ind = inversions.pop()

            # we have a clean node we can sacrifice in order to invert our inversion
            if clean:
                nums[ind] = xor

                # sacrifice the clean node
                num, xor, ind = clean.pop()
                nums[ind] = xor

        return sum(nums)
