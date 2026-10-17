from node import ListNode, DLLNode

class LinkedList:
    def __init__(self, arr=None):
        if arr:
            self.root = create_list(arr)
        else:
            self.root = None

    def create_list(self, arr):
        sentinel = curr = ListNode()
        for node in arr:
            curr.next = ListNode(node)
            curr = curr.next
        return sentinel.next

    def print_list(self):
        if not self.root:
            return ""
        
        s = ""
        curr = self.root
        while curr:
            s += curr.value
            curr = curr.next

        return s

class DoublyLinkedList:
    def __init__(self, arr=None):
        self.root = self.create_list(arr) if arr else None

    def create_list(self, arr):
        sentinel = curr = DLLNode(arr[0])
        for node in arr[1:]:
            curr.next = DLLNode(node, None, curr)
            curr = curr.next

        return sentinel

    def print_list(self):
        if not self.root:
            return ""
        
        s = ""
        curr = self.root
        while curr:
            s += curr.value
            curr = curr.next

        return s


