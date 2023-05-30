# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2) :
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            current.next = ListNode(carry % 10)
            current = current.next
            carry //= 10

        return dummy.next

# Example 1    
l1 = [2,4,3]
l2 = [5,6,4]
# Expected Output: [7,0,8]
# Explanation: 342 + 465 = 807.
