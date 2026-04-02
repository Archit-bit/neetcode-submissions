# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        carry = 0
        
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            node_val = total % 10
            cur.next = ListNode(node_val)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
            
            # Your specific logic block, patched to work:
            if not (l1 and l2):
                
                # 1. Loop through the rest of l1 to let the carry ripple
                while l1:
                    total = l1.val + carry
                    carry = total // 10
                    cur.next = ListNode(total % 10)
                    cur = cur.next
                    l1 = l1.next
                
                # 2. Loop through the rest of l2 to let the carry ripple
                while l2:
                    total = l2.val + carry
                    carry = total // 10
                    cur.next = ListNode(total % 10)
                    cur = cur.next
                    l2 = l2.next
                
                # 3. If there is a final carry left over, attach it at the very end
                if carry:
                    cur.next = ListNode(carry)
                    # Reset carry to 0 so it doesn't trigger repeatedly if the outer loop somehow kept going
                    carry = 0 
                    
        return head.next