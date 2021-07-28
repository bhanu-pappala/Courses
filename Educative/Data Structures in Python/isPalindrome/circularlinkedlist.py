class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        curr = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    curr.next = self.head.next
                    self.head = self.head.next
            else:
                curr = self.head
                prev = None
                while curr.next != self.head:
                    prev = curr
                    curr = curr.next
                    if curr.data == key:
                        prev.next = curr.next
                        curr = curr.next

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        count = 0

        prev = None
        curr = self.head

        while curr and count < mid:
            count += 1
            prev = curr
            curr = curr.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while curr.next != self.head:
            split_cllist.append(curr.data)
            curr = curr.next
        split_cllist.append(curr.data)

        self.print_list()
        print('\n')
        split_cllist.print_list()

    def remove_node(self, node):
        if self.head == node:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            if self.head == self.head.next:
                self.head = None
            else:
                curr.next = self.head.next
                self.head = self.head.next
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
                if curr == node:
                    prev.next = curr.next
                    curr = curr.next

    def josephus_circle(self, step):
        curr = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                curr = curr.next
                count += 1
            print("KILL: " + str(curr.data))
            self.remove_node(curr)
            curr = curr.next

    def is_circular_linked_list(self, input_list):
        if input_list.head :
            curr = input_list.head
            while curr.next:
                curr = curr.next
                if curr == input_list.head:
                    return True
            return False
        else:
            return False


cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)


cllist.josephus_circle(2)
cllist.print_list()
