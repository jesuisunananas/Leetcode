from __init__ import ListNode, LinkedList

class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self, arr=None):
        self.sentinel = ListNode()
        self.size = 0
        if arr:
            self.sentinel.next = LinkedList(arr[::-1]).root
            self.size = len(arr)

    def push(self, value):
        new_node = ListNode(value)
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise EmptyStackError("Cannot pop from empty stack")
        node_to_remove = self.sentinel.next
        self.sentinel.next = self.sentinel.next.next
        self.size -= 1
        return node_to_remove.value

    def peek(self):
        if self.size == 0:
            raise EmptyStackError("Cannot peek empty stack")
        return self.sentinel.next.value

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
    
