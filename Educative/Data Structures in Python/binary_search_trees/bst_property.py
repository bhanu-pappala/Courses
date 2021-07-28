class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, curr_node, data):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(curr_node.left, data)
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(curr_node.right, data)
        else:
            print("The value is already in there.")

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, curr_node):
        if curr_node:
            self._inorder_print_tree(curr_node.left)
            print(str(curr_node.data))
            self._inorder_print_tree(curr_node.right)

    def find(self, data):
        if self.root:
            is_found = self._find(self.root, data)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, curr_node, data):
        if data > curr_node.data and curr_node.right:
            return self._find(curr_node.right, data)
        elif data < curr_node.data and curr_node.left:
            return self._find(curr_node.left, data)
        if data == curr_node.data:
            return True

    def is_bst_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.data
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(self.root)
bst = BST(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(bst.is_bst_satisfied())
print(tree.is_bst_satisfied())
