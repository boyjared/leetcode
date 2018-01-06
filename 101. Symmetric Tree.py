# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isReflection(left, right):
            if(left == None and right == None):
                return True
            elif(left == None or right == None):
                return False
            else:
                return (left.val == right.val and isReflection(left.left, right.right) and isReflection(right.left, left.right))

        return isReflection(root, root)