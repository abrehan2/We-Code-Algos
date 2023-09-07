# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeElements(self, head, val):       
        dummy = ListNode(next=head)
        prev, current = dummy, head

        while current:
            if current.val == val:
               prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy.next

        
            
        