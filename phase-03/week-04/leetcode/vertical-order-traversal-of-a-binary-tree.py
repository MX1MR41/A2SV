class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        # iterates through the tree and populates the cols dictionary
        # for each column, we appen the node along with its coordinates
        def dfs(head, r, c):
            if head:
                cols[c].append([c, r, head.val])

                if head.left:
                    dfs(head.left, r + 1,  c - 1)
                
                if head.right:
                    dfs(head.right, r + 1,  c + 1)
                
        dfs(root, 0,0)

        for i in cols:
            # since the format is [c,r,val], it will be sorted by column first by default
            # then row then val
            cols[i].sort() 

        cols = sorted(cols.items())
        ans = []
        for i in cols:
            x , y=  i
            temp = [j[-1] for j in y]
            ans.append(temp)

        return ans
                    
