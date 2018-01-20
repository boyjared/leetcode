# Definition for singly-linked list.

def printNode(l):
    while l != None:
        print(l.val)
        l = l.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        duplicate = set()
        new = head
        new_next = None
        if new == None:
            return None
        elif new != None:
            duplicate.add(new.val)
        if new.next != None:
            new_next = new.next
        while(new_next != None):
            if new_next.val in duplicate:
                if new_next.next != None:
                    new.next = new_next.next
                    new_next = new_next.next
                else:
                    new.next = None
                    new_next = new_next.next
            else:
                duplicate.add(new_next.val)
                new = new.next
                new_next = new_next.next
        return head


l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
# l4 = ListNode(3)
# l5 = ListNode(3)
l1.next = l2
l2.next = l3
# l3.next = l4
# l4.next = l5

solution = Solution()
res = solution.deleteDuplicates(l1)
printNode(res)