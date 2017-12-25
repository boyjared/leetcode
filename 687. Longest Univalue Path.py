class Solution:
    def longestUnivaluePath(self, root):
        self.max_length = 0

        def longest_edge_length(node):
            if node == None:
                return 0
            left_length = longest_edge_length(node.left)
            right_length = longest_edge_length(node.right)
            left_arrow = right_arrow = 0
            if node.left == None:
                left_length = 0
            if node.right == None:
                right_length = 0
            if node.left != None and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right != None and node.right.val == node.val:
                right_arrow = right_length + 1
            self.max_length = max(self.max_length, left_arrow+right_arrow)
            return max(left_arrow, right_arrow)

        longest_edge_length(root)
        return self.max_length


