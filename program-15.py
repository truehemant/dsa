#Q15:  Write a program in python to search an existing element in a single linked list.

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
                print(f'Data = {current.data}')
                current = current.next


    def find_node(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                print(f'Element found at node {index+1}')
                return
            current = current.next
            index += 1

        print(f'Element {value} is not in the list')

        


print('Linked List: Search an element in Singly Linked list.')
print('-------------------------------------------')
n = int(input("Enter the number of nodes: "))
linked_list = LinkedList()

for i in range(n):
    value = int(input(f"Enter data for node {i+1}: "))
    linked_list.append(value)

print('Data Entered in the list: ')
linked_list.display()

# search element

number = int(input('Enter number to be searched: '))
linked_list.find_node(number)

'''
OUTPUT

Linked List: Search an element in Singly Linked list.
-------------------------------------------
Enter the number of nodes: 3
Enter data for node 1: 2
Enter data for node 2: 5
Enter data for node 3: 8
Data Entered in the list:
Data = 2
Data = 5
Data = 8
Enter number to be searched: 5
Element found at node 2

'''
