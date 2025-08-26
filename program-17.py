#Q17: Write a program in python to insert a new node at the begining in a doubly linked list. 

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
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def display(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        
        while current:
            print(f'node = {current.data}')
            current = current.next
        print()

print('Doubly Linked List: insert a new node at the beginning in a doubly linked list.')
print('-------------------------------------------')
n = int(input("Enter the number of nodes: "))
linked_list = DoublyLinkedList()

for i in range(n):
    value = int(input(f"Enter data for node {i+1}: "))
    linked_list.insert(value)

print('\nData Entered in the list: ')
linked_list.display()

first_node_value = int(input("Input the data for the first node: "))
linked_list.insert_at_beginning(first_node_value)

print('After insertion the new list are: ')
linked_list.display()

'''
OUTPUT

Doubly Linked List: insert a new node at the beginning in a doubly linked list.
-------------------------------------------
Enter the number of nodes: 3
Enter data for node 1: 2
Enter data for node 2: 5
Enter data for node 3: 8

Data Entered in the list:
node = 2
node = 5
node = 8

Input the data for the first node: 1
After insertion the new list are:
node = 1
node = 2
node = 5
node = 8


'''
