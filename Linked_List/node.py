class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class DLLNode(ListNode):
    def __init__(self, value=None, next=None, prev=None):
        super().__init__(value, next)
        self.prev = prev
