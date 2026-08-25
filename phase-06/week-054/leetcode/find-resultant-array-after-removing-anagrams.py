class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        arr = []
        for word in words:
            vector = [0] * 26 
            for i in word:
                vector[ord(i) - 97] += 1

            arr.append((word, vector))

        stack = []

        for word, vector in arr[::-1]:
            while stack and stack[-1][-1] == vector:
                stack.pop()

            stack.append((word, vector))

        return [pair[0] for pair in stack[::-1]]

        
