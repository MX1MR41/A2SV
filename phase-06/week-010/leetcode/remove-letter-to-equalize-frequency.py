class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            count = defaultdict(int)
            for j in range(len(word)):
                if j == i:
                    continue

                count[word[j]] += 1
            
            if len(set(count.values())) == 1:
                return True


        return False
        
