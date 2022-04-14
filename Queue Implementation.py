class Node():
    def stacky(value):
        dict = {
            'value': value,
            'next': None
        }
        return dict

class Queue(Node):
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        newNode = Node.stacky(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last['next'] = newNode
            self.last = newNode
        self.length += 1
        return self


    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            firstNode = self.first['next']
            self.first = firstNode
        self.length -= 1
        return self
            


    def isEmpty(self):
        if self.first:
            return False
        else:
            return True


myQueue = Queue()
myQueue.enqueue(5)
myQueue.enqueue('kbye')
myQueue.enqueue('aha moment')


print(myQueue.last)

