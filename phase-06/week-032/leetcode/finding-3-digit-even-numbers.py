class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        res = set()

        count = Counter(digits)

        for third in range(0, 10, 2):
            if count[third] == 0:
                continue

            count[third] -= 1

            for second in range(10):
                if count[second] == 0:
                    continue

                count[second] -= 1

                for first in range(1, 10):
                    if count[first] == 0:
                        continue

                    num = int(str(first) + str(second) + str(third))

                    res.add(num)

                count[second] += 1


            count[third] += 1


        return sorted(list(res))


            
            
