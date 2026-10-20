import deque
from tree_node import TreeNode 

class Tree:
    def __init__(self, arr=None):


    def create_tree(self, root):
        counter = 0
        q = deque(root)
        start = curr = None

        while q:
            for i in range(pow(2, counter)):
                node = q.popleft()
                curr = node
                if node.left:
                    curr.left = node.left
                if node.right:
                    curr.right = node.right

            counter += 1

    def print_tree(self, root):
        counter = 0
        q = deque([root])

        while q:
            s = ""

            for i in range(pow(2, counter)):
                node = q.popleft()
                if not node:
                    break

                s += str(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            print(s)
            counter += 1




