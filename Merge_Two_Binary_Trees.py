# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self,val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solutions(object):
    def mergeTrees(self, root1, root2):

        if not root1 and root2:
            return root2
        if not root2 and root1:
            return root1
        if not root1 and not root2:
            return

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1