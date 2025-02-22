class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head 
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end= " -> ")
            temp = temp.next
        print("None")

#example
ll = LinkedList()
ll.insert("Pizza")
ll.insert("Burger")
ll.insert("Fries")
ll.display()