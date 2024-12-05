# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current = head
        # print(current.val)
        while current:
            stack.append(current.val)
            current = current.next
        # print(stack)
        if stack == stack[::-1]:
            return True
        else:
            return False
        