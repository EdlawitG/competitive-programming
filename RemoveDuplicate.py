# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0,head)
        ptr1 = start
        ptr2 = head
        while ptr2:
            if ptr2.next and ptr2.val == ptr2.next.val:
                while ptr2.next and ptr2.val == ptr2.next.val:
                    ptr2= ptr2.next
                ptr1.next = ptr2.next
            else:
                ptr1 = ptr1.next
            ptr2 = ptr2.next
        return start.next
                
                    
            
