class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # hashmap
        # construct a "universal" counter dictionary for all the words in word2
        # such that the value of universal[letter] must be the max freq of that letter among words2
        # then for every word in word1, compare to see if all the letters in the universe are
        # present in that word, if so then it is an answer  
        universe = defaultdict(int)
        for word in words2:
            count = Counter(word)
            for letter, cnt in count.items():
                universe[letter] = max(universe[letter], cnt)


        res = []
        for word in words1:
            count = Counter(word)
            for letter, cnt in universe.items():
                if cnt > count[letter]:
                    break

            else:
                res.append(word)

        return res
        
