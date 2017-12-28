# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def searchBT(node, path, result):
            if node.left == None and node.right == None:
                result.append(path + str(node.val))
            if node.left != None:
                searchBT(node.left, path + str(node.val) + "->" , result)
            if node.right != None:
                searchBT(node.right, path + str(node.val) + "->", result)

        if root != None:
            answer = []
            searchBT(root, "", answer)
            return answer
        else:
            return []
