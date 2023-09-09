# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
       prev, current = head, head
       while current and current.next:
           prev = prev.next
           current = current.next.next

       return prev 