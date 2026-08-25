class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least = float('inf')
        result = []
        for i in list1:
            if i in list2:
                if list1.index(i) + list2.index(i) < least:
                    least = list1.index(i) + list2.index(i)
                    if not result:
                        result.append(i)
                    else:
                        result.pop()
                        result.append(i)

                elif list1.index(i) + list2.index(i) == least:
                    result.append(i)

        return result