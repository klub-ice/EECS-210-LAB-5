from binarynode import *

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, value):
        # self._rec_add(self._root, value)
        # FIX this method to check if entire tree empty before recursion
        if self._root is None:
            self._root = BinaryNode(value)
        else:
            self._rec_add(self._root, value)

    def _rec_add(self, node, value):
        if value == node.data:
            raise ValueError('Value already present')
        elif value < node.data:
            if node.left is not None:
                self._rec_add(node.left, value)
            else:
                node.left = BinaryNode(value)
        elif value > node.data:
            if node.right is not None:
                self._rec_add(node.right, value)
            else:
                node.right = BinaryNode(value)

    def find(self, target):
        # calls the private search method to find the target
        return self._rec_search(target, self._root)

    def _rec_search(self, target, current):
        # recursively searches through tree for target from root node
        if current is None:
            return False
        elif current.entry is target:
            return True
        else:
            return self._rec_search(target, current.left) or self._rec_search(target, current.right)

    def count_nodes(self):
        # returns a count of nodes
        return self._rec_count_nodes(self._root)

    def _rec_count_nodes(self, current):
        # recursive count method
        if current is None:
            return 0
        else:
            return self._rec_count_nodes(current.left) + self._rec_count_nodes(current.right) + 1
