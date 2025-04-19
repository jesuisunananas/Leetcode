# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"

class Solution:
    def reverseList(self, head):
        tail = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = tail
            tail = curr
            curr = temp
        return tail

sol = Solution()
print(sol.reverseList(ListNode(0, ListNode(1, ListNode(2, ListNode(3, None))))))
print(sol.reverseList(ListNode()))

'''
3 -> 2 -> 1 -> 0
0
'''