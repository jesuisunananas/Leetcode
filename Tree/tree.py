import deque
from tree_node import TreeNode 

class Tree:
    def __init__(self, arr=None):
        self.root = TreeNode()
        if arr:
            self.root = create_tree(arr) 

    def create_tree(self, arr):
        if arr[0] == "N":
            return None

        index = 1
        root = TreeNode(int(arr[0]))
        q = deque([root])

        while q:
            node = q.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(arr[index]))
                q.append(node.left)
            index += 1
            if vals[index] != "N":
                node.right = TreeNode(int(arr[index]))
                q.append(node.right)
            index += 1

        return root

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




