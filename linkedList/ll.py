class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtHead(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def insertAtTail(self, data):
        newNode = Node(data)
        if (!self.head):
            self.head = newNode
        current = self.head
        while(current.next):
            current = current.next
        
