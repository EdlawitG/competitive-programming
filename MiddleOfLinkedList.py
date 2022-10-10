# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        start = head
        while not start == None:
            length +=1
            start = start.next
        mid = int(length//2)
        for i in range(mid):
            head = head.next
        return head
