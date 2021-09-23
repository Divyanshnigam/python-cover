

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()
    def displ(self):
        return self


s1=Stack()
s1.disp()
s1.pop()
