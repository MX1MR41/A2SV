class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        HASH = defaultdict(int)

        for i in cpdomains:

            cnt, doms = i.split()
            dots = doms.count(".")
            HASH[doms] += int(cnt)
            
            for j in range(dots):
                doms = doms[doms.index(".") + 1:]
                HASH[doms] += int(cnt)

  

        return [f"{cnt} {dom}" for dom, cnt in HASH.items()]


# Trie solution

class TrieNode():
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, count, dom):
        doms = reversed(dom.split("."))
        root = self.root

        for d in doms:
            if d not in root.children:
                root.children[d] = TrieNode()
            root = root.children[d]
            root.count += count
        

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        trie = Trie()

        for rep in cpdomains:
            count, doms = rep.split()
            count = int(count)
            trie.insert(count, doms)


        def dfs(node, suffix):
            ans = [(node.count, suffix)]

            for ch in node.children:
                ans.extend(dfs(node.children[ch], ch + "." + suffix))

            return ans


        res = []
        for ch in trie.root.children:
            res.extend(dfs(trie.root.children[ch], ch))


        cleaned = []
        for count, dom in res:
            cleaned.append(str(count)+ " " + dom)

        return cleaned



        
        


        
