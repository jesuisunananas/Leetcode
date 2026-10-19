import sys
import os

target_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Linked_List"))

if target_path not in sys.path:
    sys.path.insert(0, target_path)

from node import ListNode, DLLNode
from linked_list import LinkedList, DoublyLinkedList
