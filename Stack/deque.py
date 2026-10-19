from __init__ import DLLNode, DoublyLinkedList

class Deque:
    def __init__(self, arr=None, maxLen):
       self.size = 0
       self.start = DLLNode()
       self.end = DLLNode()
       if arr:
           self.start.next, self.end.prev = DoublyLinkedList(arr)
           self.start.next.prev = self.start
           self.end.prev.next = self.end
           self.size = len(arr)

    def append(self, value):
        pass

    def appendleft(self, value):
        pass

    def extend(self, iterable):
        pass

    def extendleft(self, iterable):
        pass

    def popleft(self):
        pass

    def pop(self):
        pass

    def remove(self, value):
        pass

    def clear(self):
        pass

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
