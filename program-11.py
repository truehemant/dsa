'''
Q11: Write a program in python to insert a new node at the begining of Simply linked list.

The test data and expected output :
input the number of nodes: 3
input data for node 1 : 5
input data for node 2 : 6
input data for node 3 : 7

Data entered in the list are
Data = 5
Data = 6 
Data = 7 

input data to insert at the begining: 4
Data after inserted in the list
Data = 4
Data = 5
Data = 6
Data = 7

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
                print(f' Data = {current.data}')
                current = current.next
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node



print('Linked List: insert a new node at the begining of a Singly linked list: ')
print('-------------------------------------------')
n = int(input("Enter the number of nodes: "))
linked_list = LinkedList()

for i in range(n):
    value = int(input(f"Enter data for node {i+1}: "))
    linked_list.append(value)

print('Data Entered in the list: ')
linked_list.display()

# insert at begining
data = int(input("\nInput data to insert at the begining of the list: ")) 
linked_list.insert_at_beginning(data)
print('Data after inserted in the list are: ')
linked_list.display()



'''
OUTPUT

Linked List: insert a new node at the begining of a Singly linked list:
-------------------------------------------
Enter the number of nodes: 3
Enter data for node 1: 5
Enter data for node 2: 6
Enter data for node 3: 7
Data Entered in the list:
 Data = 5
 Data = 6
 Data = 7

Input data to insert at the begining of the list: 4
Data after inserted in the list are:
 Data = 4
 Data = 5
 Data = 6
 Data = 7

'''
