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
        if (not self.head):
            self.head = newNode
            self.tail = newNode
            return

        current = self.head
        while(current.next):
            current = current.next
        current.next = newNode
        self.tail = newNode

    def insertAtPosition(self,data,position):
        if(position <= 0):
            self.insertAtHead(data)
            return
        newNode = Node(data)
        current = self.head
        temp = 1
        while(current.next and temp <= position):
            if(temp+1 == position):
                newNode.next = current.next
                current.next = newNode
                return
                
            current = current.next
            temp +=1
    
    def display(self):
        current = self.head
        while current:
            
            print(current.data, end=" -> ")
            current = current.next
        print("end")

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def reverseLL(self):
        current = self.head
        prev = None

        self.reverseRecursion(current, prev)

    def reverseRecursion(self, current, prev):
        if current is None:
            self.head = prev
            return
        self.reverseRecursion(current.next, current)
        current.next = prev
    
    def findMiddle(self):
        fast_ptr = self.head
        slow_ptr = self.head

        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        print(slow_ptr.data)


    def deleteNode(self,pos):
        temp = 1
        tempNode = self.head
        while(temp < pos-1):
            tempNode = tempNode.next
            temp += 1
        tempNode.next = tempNode.next.next
        

linked_list = LinkedList()

# Insert elements at the head
linked_list.insertAtHead(10)
linked_list.insertAtHead(5)
linked_list.insertAtHead(2)
linked_list.insertAtHead(1)

# Insert elements at the tail
linked_list.insertAtTail(15)
linked_list.insertAtTail(20)

# Insert elements at a specific position
linked_list.insertAtPosition(7, 2)
linked_list.insertAtPosition(25, 5)

# Display the linked list
linked_list.display()
linked_list.findMiddle()
# linked_list.reverse()
# linked_list.display()
# linked_list.reverseLL()
# linked_list.display()

