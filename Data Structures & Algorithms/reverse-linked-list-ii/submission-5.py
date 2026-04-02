# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        dummy=ListNode(0,head)
        leftprev=dummy
        for _ in range (left-1):
            leftprev=cur
            cur=cur.next
        prev=None
        for _ in range(right-left+1):
            next_node=cur.next
            cur.next=prev
            prev,cur=cur,next_node
        leftprev.next.next=cur
        leftprev.next=prev
        return dummy.next
        

            
        
