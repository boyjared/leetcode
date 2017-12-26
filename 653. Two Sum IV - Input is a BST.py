class Solution:
    def findTarget(self, root, k):
        l = []
        def inOrder(root):
            if root != None:
                inOrder(root.left)
                l.append(root.val)
                inOrder(root.right)
            return l
        order_list = inOrder(root)
        # print(order_list)
        length = len(order_list)
        l = 0
        r = length - 1
        while(l < r):
            if order_list[l] + order_list[r] == k:
                return True
            elif order_list[l] + order_list[r] < k:
                l = l + 1
            elif order_list[l] + order_list[r] > k:
                r = r - 1
        return False
