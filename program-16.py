#Q16: Write a program in python to create and display doubly a doubly Linked List.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)
        if self.head is None:  
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current
    
    def display(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        
        while current:
            print(f'node = {current.data}')
            current = current.next
        print()

print('Doubly Linked List: Create and display a doubly linked List.')
print('-------------------------------------------')



n = int(input("Enter the number of nodes: "))
linked_list = DoublyLinkedList()

for i in range(n):
    value = int(input(f"Enter data for node {i+1}: "))
    linked_list.insert(value)

print('\nData Entered in the list: ')
linked_list.display()


'''
OUTPUT

Doubly Linked List: Create and display a doubly linked List.
-------------------------------------------
Enter the number of nodes: 3
Enter data for node 1: 2
Enter data for node 2: 5
Enter data for node 3: 8

Data Entered in the list:
node = 2
node = 5
node = 8

'''
