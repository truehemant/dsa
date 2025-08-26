'''
Q10: Write a program in python to create and display single Linked list of n nodes and display it in reverse order
input the number of nodes

input data for node 1 : 5
input data for node 2 : 6
input data for node 3 : 7
expected output:

Data entered in the list are
data = 5
data = 6 
data = 7 

Data in the reverse
data = 7
data = 6
data = 5

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def reverse_display(self):
        def _reverse_display(node):
            if node is None:
                return
            _reverse_display(node.next)
            print(node.data)
        
        _reverse_display(self.head)

print('Linked List To Create and display single linked list')
print('-------------------------------------------')
n = int(input("Enter the number of nodes: "))
linked_list = LinkedList()

for i in range(n):
    value = input(f"Enter data for node {i+1}: ")
    linked_list.append(value)

print('Data Entered in the list: ')
linked_list.display()

print('\nData Entered in the list in reverse order: ')
linked_list.reverse_display()


'''
OUTPUT

Linked List To Create and display single linked list
-------------------------------------------
Enter the number of nodes: 3
Enter data for node 1: 10
Enter data for node 2: 20
Enter data for node 3: 30
Data Entered in the list:
10
20
30

Data Entered in the list in reverse order:
30
20
10

'''
