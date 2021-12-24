# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return (self.recursiveFunction(head))

    def recursiveFunction(self, head):
        previous_node = None
        while head is not None:
            temp = head
            head = head.next
            temp.next = previous_node
            previous_node = temp
        return previous_node