class Node():
    def bst(self, value):
        self.right = None
        self.left = None
        self.value = value
        dict = {
            'value' : self.value,
            'right' : self.right,
            'left' : self.left
        }
        return dict



class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        newNode = Node().bst(value)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                #Left
                if value < currentNode['value']:
                    if not currentNode['left']:
                        currentNode['left'] = newNode
                        return self
                    currentNode = currentNode['left']
                else:
                    #Right
                    if not currentNode['right']:
                        currentNode['right'] = newNode
                        return self
                    currentNode = currentNode['right'] 

    def lookup(self, value):
        if self.root == None:
            return None
        currentNode = self.root
        try:
            while True:
                if value == currentNode['value']:
                    return f'{value} exists in the tree!'
                elif value < currentNode['value']:
                    if value == currentNode['left']:
                        return f'{value} exists in the tree!'
                    currentNode = currentNode['left']
                else:
                    if value == currentNode['right']:
                        return f'{value} exists in the tree!'
                    currentNode = currentNode['right']
        except: return None

    def breadthFirstSearch(self):
        currentNode = self.root
        resultList = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            resultList.append(currentNode['value'])
            if currentNode['left']:
                queue.append(currentNode['left'])
            if currentNode['right']:
                queue.append(currentNode['right'])
        return resultList

    def breadthFirstSearchRecursive(self, queue, ilist):
        if len(queue) == 0:
            return ilist
        currentNode = queue.pop(0)
        ilist.append(currentNode['value'])
        if currentNode['left']:
                queue.append(currentNode['left'])
        if currentNode['right']:
                queue.append(currentNode['right'])
        return self.breadthFirstSearchRecursive(queue, ilist)


    def DFSinOrder(self):
        return traverseInOrder(self.root, [])

    def DFSpreOrder(self):
        return traversePreOrder(self.root, [])

    def DFSpostOrder(self):
        return traversePostOrder(self.root, [])


def traverseInOrder(node, array):
    if node['left']:
        print(node['value'])
        traverseInOrder(node['left'], array)
    array.append(node['value'])

    if node['right']:
        traverseInOrder(node['right'], array)

    return array

def traversePreOrder(node, array):
    array.append(node['value'])
    if node['left']:
        traversePreOrder(node['left'], array)

    if node['right']:
        traversePreOrder(node['right'], array)

    return array

def traversePostOrder(node, array):
    if node['left']:
        traversePostOrder(node['left'], array)

    if node['right']:
        traversePostOrder(node['right'], array)
    
    array.append(node['value'])

    return array

#                9

#        4               20

#   1       6       15      170

    #remove

myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(1)
myTree.insert(6)
myTree.insert(15)
myTree.insert(170)
print(myTree.breadthFirstSearch())
print(myTree.breadthFirstSearchRecursive([myTree.root], []))
print(myTree.DFSinOrder())
print(myTree.DFSpreOrder())
print(myTree.DFSpostOrder())