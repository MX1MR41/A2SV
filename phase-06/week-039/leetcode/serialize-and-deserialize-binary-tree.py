# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def convert(self, root):
        """Given a tree, it'll convert every node's val to make them unique
        by numbering them from 1 to n; then return their original values as a map

        """
        vals = {}
        curr = 1
        que = deque([root])
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                vals[curr] = node.val
                node.val = curr
                curr += 1

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return vals


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        # convert the tree's node's values to make them unique
        # and get the original value's of the nodes as a map
        # then serialize that map into a string of format "new_val:original_val,..."
        vals = self.convert(root)
        str_vals = ""
        for i in vals:
            str_vals += f"{i}:{vals[i]},"

        
        # store the left chilld of every node in the left string as 
        # "node:left_child,node:left_child,..."
        # do the same for the right children as well in the string right
        # and store the root's value in root_val
        # traverse in a breadth-first manner
        left = right = rootval = ""
        que = deque([root])

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if rootval == "":
                    rootval = str(node.val)

                if node.left:
                    left += f"{node.val}:{node.left.val},"
                    que.append(node.left)

                if node.right:
                    right += f"{node.val}:{node.right.val},"
                    que.append(node.right)
        
        
        return f"{rootval}|{left}|{right}|{str_vals}"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data == "":
            return None

        rootval, left, right, str_vals = data.split("|")

        nodes = {} # map every node's val to the actual node object

        root = TreeNode(int(rootval))

        nodes[int(root.val)] = root

        for l in left.split(",")[:-1]:
            par, child = l.split(":")

            par = int(par)
            child = int(child)

            if par not in nodes:
                nodes[par] = TreeNode(par)

            if child not in nodes:
                nodes[child] = TreeNode(child)

            nodes[par].left = nodes[child]

        for r in right.split(",")[:-1]:
            par, child = r.split(":")

            par = int(par)
            child = int(child)

            if par not in nodes:
                nodes[par] = TreeNode(par)

            if child not in nodes:
                nodes[child] = TreeNode(child)

            nodes[par].right = nodes[child]

        # convert the tree's nodes' values to their original values
        vals = {}
        for i in str_vals.split(",")[:-1]:
            node, val = list(map(int, i.split(":")))
            nodes[node].val = val


        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
