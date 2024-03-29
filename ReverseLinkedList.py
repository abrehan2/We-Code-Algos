# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


class Solution:
    def reverse_list(self, head):
        prev, current = None, head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev


# sol_obj = Solution();
# sol_obj.reverse_list([1,2,3,4,5])
