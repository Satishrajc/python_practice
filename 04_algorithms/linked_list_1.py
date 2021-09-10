class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

        def insert_at_end(self, data):
            self.head = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_begining(5)
    l1.insert_at_begining(6)
    l1.insert_at_begining(7)
    l1.print()
