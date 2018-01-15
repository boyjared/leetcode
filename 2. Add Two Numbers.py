# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start_l = ListNode(l1.val + l2.val)
        now_l = start_l
        l1_next = l1.next
        l2_next = l2.next

        while (l1_next != None and l2_next != None):
            new_l = ListNode(l1_next.val + l2_next.val)
            now_l.next = new_l
            now_l = new_l
            l1_next = l1_next.next
            l2_next = l2_next.next

        while (l1_next != None):
            now_l.next = l1_next
            now_l = now_l.next
            l1_next = l1_next.next

        while (l2_next != None):
            now_l.next = l2_next
            now_l = now_l.next
            l2_next = l2_next.next

        update_l = start_l
        while (update_l != None):
            if update_l.val >= 10:
                update_l.val -= 10
                if update_l.next != None:
                    update_l.next.val += 1
                else:
                    new_l = ListNode(1)
                    update_l.next = new_l
            update_l = update_l.next
        return start_l

n1 = ListNode(1)
n2 = ListNode(8)
n3 = ListNode(0)
n1.next = n2
solution = Solution()
res = solution.addTwoNumbers(n1, n3)
print(res)
