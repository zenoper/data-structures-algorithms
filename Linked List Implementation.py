
# 10 --> 5 --> 16
# Singly Linked List

class LinkedList():
  def __init__(self, value) -> None:
      super().__init__()
      self.head = {
        'value': value,
        'next': None
      }
      self.tail = self.head
      self.length = 1

  def append(self, number):
    newNode = {
      'value': number,
      'next': None
    }
    self.tail.update({'next': newNode})
    self.tail = newNode
    self.length += 1
    return self
  
  def prepend(self, value):
    newNode = {
      'value': value,
      'next': None
    }
    newNode.update({'next': self.head})
    self.head = newNode
    self.length += 1
    return self

  def printList(self):
    listarray = []
    currentNode = self.head
    while currentNode != None:
      listarray.append(currentNode['value'])
      currentNode = currentNode['next']
    return print(listarray)

  def insert(self, index, value):
    if index >= self.length:
      return self.append(value)
    if index == 0:
      return self.prepend(value)

    newNode = {
      'value': value,
      'next': None
    }
    leader = self.traverseToIndex(index-1)
    runner_up = leader['next']
    leader['next'] = newNode
    newNode['next'] = runner_up
    self.length += 1
    return self
    
  def traverseToIndex(self, index):
    counter = 0
    currentNode = self.head
    while counter != index:
      currentNode = currentNode['next']
      counter += 1
    return currentNode

  def remove(self, index):
    if index > self.length:
      return print('Index out of range!')
    if index == 0:
      pass

    leader = self.traverseToIndex(index-1)
    unwantedNode = leader['next']
    leader['next'] =  unwantedNode['next']
      
    self.length -= 1
    return self

  def reverse(self):
    if self.length == 1:
      return self.head
    first = self.head
    self.tail = self.head
    second = first['next']
    while second:
      temp = second['next']
      second['next'] = first
      first = second
      second = temp
    self.head['next'] = None
    self.head = first
    return self

myLinkedList = LinkedList(5)
myLinkedList.append(0)
myLinkedList.prepend(7)
myLinkedList.insert(2, 55)
myLinkedList.insert(50, 3)
myLinkedList.remove(1)
myLinkedList.reverse()
myLinkedList.printList()
print(myLinkedList.head)



