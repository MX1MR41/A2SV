class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                
                index1 = order.index(words[i][j])
                index2 = order.index(words[i + 1][j])

                if index1 > index2:
                    return False

                elif index1 < index2:
                    break

                elif index1 == index2 and \
                    (j == len(words[i]) - 1 or j == len(words[i + 1]) - 1) and \
                    len(words[i]) > len(words[i + 1]):
                    return False


        return True
