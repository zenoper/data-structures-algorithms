class Stack():
    def __init__(self) -> None:
        self.array = []

    def peek(self):
        if self.array:
            return self.array[-1]
        else:
            return None

    def push(self, value):
        self.array.append(value)
        return self.array

    def pop(self):
        self.array.pop()
        return self

    def isEmpty(self):
        if self.array:
            return False
        else:
            return True


class StackQueue(Stack):
    def __init__(self) -> None:
        super().__init__()
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, element):
        newNode = Stack().push(element)
        if self.length == 0:
            self.first = newNode[0]
            self.last = newNode
        else:
            self.last.append(element)
        self.length += 1
        return self

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            newNode = self.last[1]
            self.first = newNode
            return self.last.pop(0)
            
        self.length -= 1
        return self

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

myStackQueue = StackQueue()
myStackQueue.enqueue('f uuuu')
myStackQueue.enqueue('finally')
myStackQueue.enqueue('aha moment finally')
myStackQueue.dequeue()
print(myStackQueue.dequeue())
print(myStackQueue.last)