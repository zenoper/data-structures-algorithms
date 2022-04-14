class Node():
    def stacky(value):
        dict = {
            'value': value,
            'next': None
        }
        return dict

class Stack(Node):
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node.stacky(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top['next'] = holdingPointer
        self.length += 1
        return self

    def pop(self):
        if self.top == None:
            return None
        elif self.length == 1:
            self.top = None
            self.bottom = None
        else:
            newTop =  self.top['next']
            self.top = newTop
        self.length -= 1

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

myStack = Stack()
myStack.push('google.com')
myStack.push('udemy.com')
myStack.push('youtube.com')
myStack.pop()
myStack.pop()
myStack.pop()
print(myStack.length)