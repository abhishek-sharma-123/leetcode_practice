#Given the root of a binary tree, return the sum of all left leaves.
#A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return None
        sum=0
        stack=[]
        stack.append(root)
        while stack!=[]:
            current=stack.pop()
            if current.right:
                stack.append(current.right)
                if not current.right.left and not current.right.right:
                    stack.pop()
            if current.left:
                stack.append(current.left)
                if not current.left.left and not current.left.right:
                    sum+=current.left.val
                    stack.pop()
        return sum