class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circularLL:
    def __init__():
        self.head = None
        self.tail = None

    def insertAtHead(self, data):
        newNode = node(data)
        temp = self.tail
        temp.next = newNode
        newNode.next = self.head
        self.head = newNode

    def insertAtTail(self,data):
        newNode = node(data)

        temp = self.tail
        temp.next = 