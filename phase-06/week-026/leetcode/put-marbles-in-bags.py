class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # super greedy
        # let weights = [1, 2, 3, 4, 5]. There are four split points as shown by letters a to d
        # split points =>  a  b  c  d ... a is between 1 and 2, b 2 and 3, c 3 and 4, d 4 and 5
        # choosing a split point will add the sum sum of its neighboring numbers to the score
        # eg. if we chose a and c then the array becomes 1 | 2, 3 | 4, 5
        # score will become (1 + 1) + (2 + 3) + (4 + 5), we can regroup the summing nums to
        # show the individual contrbutions of each split point => 1 + (1 + 2) + (3 + 4) + 5
        # a's contribution is (1 + 2) and b's contribution is (3 + 4)
        # so choosing a split point X will add a score of X_LEFT + X_RIGHT to the tot score
        # so to get the max possible score, we choose the k-1 highest contributing split points
        # and to get the min possible score, we choose the k-1 lowest

        splits = []
        for i in range(len(weights) - 1):
            split_score = weights[i] + weights[i + 1]
            splits.append(split_score)

        splits.sort()

        n = len(weights)

        return sum(splits[(n - k):]) - sum(splits[:k - 1])
