class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head 
        else: 
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display (self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end =" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("Back to head")

#example
cll = CircularLinkedList()
cll.insert("Pizza")
cll.insert("Burger")
cll.insert("Fries")

print("Circular Linked List:")
cll.display() 