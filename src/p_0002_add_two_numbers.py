class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = node = ListNode()
        carry = 0
        while l1 is not None or l2 is not None or carry == 1:
            val = carry
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            carry = val // 10
            node.next = ListNode(val % 10)
            node = node.next
        return answer.next