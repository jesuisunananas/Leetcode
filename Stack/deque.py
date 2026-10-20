from __init__ import DLLNode, DoublyLinkedList

class EmptyQueueException(Exception):
    pass

class Deque:
    def __init__(self, arr=None, maxLen):
       self.size = 0
       self.start = DLLNode()
       self.end = DLLNode()
       self.start.next = self.end
       self.end.prev = self.start
       if arr:
           self.start.next, self.end.prev = DoublyLinkedList(arr)
           self.start.next.prev = self.start
           self.end.prev.next = self.end
           self.size = len(arr)

    def append(self, value):
        new_node = DLLNode(value, self.end, self.end.prev)
        self.end.prev.next = new_node
        self.end.prev = new_node
        size += 1

    def appendleft(self, value):
        new_node = DLLNode(value, self.start.next, self.start)
        self.start.next.prev = new_node
        self.start.next = new_node
        size += 1

    def extend(self, iterable):
        for node in iterable:
            self.append(node)

    def extendleft(self, iterable):
        for node in iterable:
            self.appendLeft(node)

    def popleft(self):
        if self.size == 0:
            raise EmptyQueueException("Cannot pop from empty queue")
        node_to_remove = self.start.next
        self.start.next = self.start.next.next
        self.start.next.prev = self.start
        return node_to_remove.value

    def pop(self):
        if self.size == 0:
            raise EmptyQueueException("Cannot pop from empty queue")
        node_to_remove = self.end.next
        self.end.prev = self.end.prev.prev
        self.end.prev.next = self.end
        return node_to_remove.value

    def remove(self, value):
        if self.size == 0:
            raise EmptyQueueException("Cannot remove from empty queue")
        curr = self.start
        while curr.next.val != value:
            curr = curr.next
        curr.next = curr.next.next
        curr.next.prev = curr

    def clear(self):
        self.start.next = self.end
        self.end.prev = self.start

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
