# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        input=[]
        while head:
            input.append(head.val)
            head=head.next
        output=input[::-1]
        return True if input==output else False