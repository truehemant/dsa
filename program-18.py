# Q18: Write a program in python to delete a node from the last in the doubly link list.

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
    
    def delete_from_end(self):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head

        if current.next is None: 
            self.head = None
            return
        while current.next:
            current = current.next
        current.prev.next = None
    
    def display(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        
        while current:
            print(f'node = {current.data}')
            current = current.next
        print()



print('Doubly Linked List: delete a node from the last in the doubly link list.')
print('-------------------------------------------')
n = int(input("Enter the number of nodes: "))
linked_list = DoublyLinkedList()

for i in range(n):
    value = int(input(f"Enter data for node {i+1}: "))
    linked_list.insert(value)

print('\nData Entered in the list: ')
linked_list.display()

print("After the deletion the new list are: ")
linked_list.delete_from_end()
linked_list.display()

'''
OUTPUT

Doubly Linked List: delete a node from the last in the doubly link list.
-------------------------------------------
Enter the number of nodes: 3
Enter data for node 1: 1
Enter data for node 2: 2
Enter data for node 3: 3

Data Entered in the list:
node = 1
node = 2
node = 3

After the deletion the new list are:
node = 1
node = 2

'''

