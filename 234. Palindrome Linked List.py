# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = []
        if head == None:
            return True
        else:
            while(head != None):
                s.append(head.val)
                head = head.next
            order_s = s.copy()
            s.reverse()
            return (order_s == s)