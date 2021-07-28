class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ''
        for i in range(len(self.items)):
            s += str(self.items[i].value) + '-'
        return s


