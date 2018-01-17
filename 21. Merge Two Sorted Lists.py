# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = None
# l2 = ListNode(2)
# l3 = ListNode(4)
# l1.next = l2
# l2.next = l3

l4 = None
# l5 = ListNode(3)
# l6 = ListNode(4)
# l4.next = l5
# l5.next = l6

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start_node = ListNode(0)
        new_node = start_node
        while(l1 != None and l2 != None):
            if l1.val < l2.val:
                new_node.next = ListNode(l1.val)
                l1 = l1.next
                new_node = new_node.next
            elif l1.val > l2.val:
                new_node.next = ListNode(l2.val)
                l2 = l2.next
                new_node = new_node.next
            else:
                new_node.next = ListNode(l1.val)
                new_node.next.next = ListNode(l2.val)
                new_node = new_node.next.next
                l1 = l1.next
                l2 = l2.next

        while(l1 != None):
            new_node.next = ListNode(l1.val)
            l1 = l1.next
            new_node = new_node.next


        while (l2 != None):
            new_node.next = ListNode(l2.val)
            l2 = l2.next
            new_node = new_node.next

        return start_node.next

solution = Solution()
res = solution.mergeTwoLists(l1, l4)
print(res)
