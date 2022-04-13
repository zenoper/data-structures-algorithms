class Array():
    def __init__(self) -> None:
        self.length = 0
        self.data = {}


    def get(self, index):
        return self.data[index]

    def push(self, value):
        self.data[self.length] = value
        self.length += 1
        return self.length

    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)

    def shiftItems(self, index):
        while index < self.length - 1:
            self.data[index] = self.data[index + 1]
            index += 1
        del self.data[self.length - 1]

myArray = Array()
myArray.push(5)
myArray.push(10)
myArray.push('yello')
myArray.push('fine')
myArray.delete(0)

print(myArray.data)
