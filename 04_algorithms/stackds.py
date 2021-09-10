# YouTube Video: https://www.youtube.com/watch?v=lVFnq4zbs-g
"""
Stack Data Structure.
GIT: https://github.com/vprusso/youtube_tutorials/tree/master/data_structures
"""


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items
