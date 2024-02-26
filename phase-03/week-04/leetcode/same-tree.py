class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # in case both nodes are empty; they do happen to be the same tree
        if not p and not q:
            return True
        # since we've eliminated the possibility of both of them being empty;
        # this time, if either is empty and the other is not, then they are not the same
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        # traverse noth directions independently and return their conjuction
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

            

        