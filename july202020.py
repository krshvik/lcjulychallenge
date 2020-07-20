class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val == val:
            thead = head
            head = head.next 
            thead.next = None 
        
        if head is None:
            return head

        thead = head 
        while head is not None:
            if head.next is not None:
                if head.next.val == val:
                    head.next = head.next.next
                else:
                    head = head.next
            else:
                head = head.next 
        
        return thead             