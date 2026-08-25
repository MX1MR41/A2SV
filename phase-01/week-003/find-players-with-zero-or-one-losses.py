class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won = set()
        lost = defaultdict(int)

        for i in matches:
            won.add(i[0])
            lost[i[1]] += 1


        list2 = [i for i in lost if lost[i]==1]
        list1 = [i for i in won if i not in lost]

        ans = [sorted(list1), sorted(list2)]

        return ans



        