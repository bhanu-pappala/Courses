class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_value):
        if self.root is None:
            self.root = Node(new_value)
        else:
            self.insert_helper(self.root, new_value)

    def insert_helper(self, current, new_value):
        if current.data < new_value:
            if current.right:
                self.insert_helper(current.right, new_value)
            else:
                current.right = Node(new_value)
        else:
            if current.left:
                self.insert_helper(current.left, new_value)
            else:
                current.left = Node(new_value)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)

bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.search(9))
print(bst.search(14))
