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

    #remove

myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(1)
myTree.insert(6)
myTree.insert(15)
myTree.insert(170)
print(myTree.lookup(4))






#                9

#        4               20

#    1      6       15      170
