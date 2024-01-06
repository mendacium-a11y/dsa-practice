class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtHead(self, data):
        newNode = node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            temp_node = self.head
            temp_node.prev = newNode
            self.head = newNode
            newNode.next = temp_node
    
    def insertAtTail(self,data):
        newNode = node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            temp_node = self.tail
            temp_node.next = newNode
            newNode.prev = temp_node
            self.tail = newNode

    def insertAtPosition(self, pos, data):
        if pos < 0:
            raise ValueError("out of bounds")

        newNode = node(data)
        
        if pos == 0:
            newNode.next = self.head
            if self.head:
                self.head.prev = newNode
            self.head = newNode

            if self.tail is None :
                self.tail = newNode
        
        temp = 0
        current = self.head
        while temp < pos-1 and current:
            current = current.next
            temp += 1
        
        if current is None:
            raise ValueError("out of bounds")

        newNode.next = current.next

        if current.next:
            current.next.prev = newNode
        current.next = newNode
        newNode.prev = current

    def deleteNode(self, data):
        current = self.head

        while current and current.data is not data:
            current = current.next
        
        if current is None:
            raise ValueError("Not in ll")
        
        if current.prev is None:
            self.head = current.next
        else:
            current.prev.next = current.next

        if current.next is None:
            self.tail = current.prev
        else:
            current.next.prev = current.prev
        
        current.next = None
        current.prev = None

    def printList(self):
        current = self.head
        while current:
            print(f"{current.data}->", end="")
            current = current.next
        print("end")


ll = linkedlist()
ll.insertAtHead(4)
ll.insertAtHead(5)
ll.insertAtHead(6)
ll.insertAtTail(1)
ll.insertAtTail(2)
ll.insertAtPosition(2, 9)
ll.insertAtPosition(5, 10)
ll.deleteNode(9)
ll.deleteNode(22)

ll.printList()