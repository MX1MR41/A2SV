
from collections import defaultdict
class Solution:
    def findOrder(self,alien_dict, N, K):
        g = defaultdict(list)
        
        letters = set()
        # store all letters
        for word in alien_dict:
            letters.update(set(word))
            
        # comparison of adjacent words will suffice instead of quadratic comparison
        # because the words are already sorted
        for i in range(N-1):
            curr, nxt = alien_dict[i], alien_dict[i+1]
            len_curr, len_nxt = len(curr), len(nxt)
    
            for j in range(min(len_curr, len_nxt)):
                # the first instance of different letters in the adjacent words
                # hence we know that the first word's letter comes first 
                # so make an edge from it to the next word's letter
                if curr[j] != nxt[j]:
                    g[curr[j]].append(nxt[j])
                    break
                
        visited = set()
        order = []
        
        # topological sorting using dfs
        # dfs, because we can't use bfs and start from "nodes" that have 0 indegrees
    
        def dfs(letter):
            if letter in visited: return
            visited.add(letter)
            neis = g[letter]
            
            for nei in neis:
                dfs(nei)
                
            order.append(letter)
        
            
        for letter in letters:

            dfs(letter)
            
        return order[::-1]


