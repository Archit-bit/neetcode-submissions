# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second= slow
        prev = None
        
        while second:
            next_node=second.next
            second.next=prev
            prev=second
            second=next_node
        slow=head
        
        while prev:
            if slow.val!=prev.val:
                return False
            slow=slow.next
            prev=prev.next
        return True


            
        