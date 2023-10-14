# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        leftT, rightT = left, right

        while head:
            if head.val < x:
                leftT.next=head
                leftT=leftT.next
            else:
                rightT.next=head
                rightT=rightT.next
            head=head.next
        
        leftT.next=right.next
        rightT.next = None

        return left.next
