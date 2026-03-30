"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping={None: None}
        dummy = Node(0)
        copy=dummy
        cur = head
        while cur:
            mapping[cur] = Node(cur.val)
            
            cur =cur.next
              
        cur = head
        while cur:
            copy= mapping[cur]
            copy.next=mapping[cur.next]
            copy.random=mapping[cur.random]
            cur = cur.next
        return mapping[head]
        
             
        
        