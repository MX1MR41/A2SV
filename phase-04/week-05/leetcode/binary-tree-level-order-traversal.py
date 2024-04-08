# RECURSIVE APPROACH

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levs = defaultdict(list)
        MAX_LEV = 0
        def dfs(node, lev):
            nonlocal MAX_LEV
            if node:

                MAX_LEV = max(lev, MAX_LEV)
                levs[lev].append(node.val)

                if node.left: dfs(node.left, lev + 1)
                if node.right: dfs(node.right, lev + 1)

        dfs(root, 0)
        res = []
 

        for lev in range(MAX_LEV+1):
            if levs[lev]: res.append(levs[lev])

        return res


# ITERATIVE APPROACH

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levs = defaultdict(list)
        MAX_LEV = 0
        
        stk = [(root, 0)]

        while stk:
            node, lev = stk.pop()
            if node:
                temp = []

                MAX_LEV = max(lev, MAX_LEV)
                levs[lev].append(node.val)
                if node.left: temp.append((node.left, lev+1))
                if node.right: temp.append((node.right, lev + 1))
                stk.extend(temp[::-1])



        res = []
 

        for lev in range(MAX_LEV+1):
            if levs[lev]: res.append(levs[lev])

        return res
