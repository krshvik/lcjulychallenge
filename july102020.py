"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        ret = self.flatlist(head)
        if ret == []:
            return None
        head = Node(ret[0])
        thead = head
        ret = ret[1:]
        while len(ret) > 0:
            node2 = Node(ret[0])
            head.next = node2
            node2.prev = head 
            head = node2
            ret = ret[1:]
            
        return thead         
        
    def flatlist(self,head):
        ret = []
        if head is None:
            return []
        while head is not None:
            ret.append(head.val)
            ret = ret + self.flatlist(head.child)
            head = head.next
        return ret 