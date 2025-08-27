# Q22: Write a program in python to search an element in a Circular Linked List.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            self.head.next = self.head  # Point to itself
        else:
            temp = self.head
            while temp.next != self.head:  # Traverse until last node
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # Make it circular

    def display(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        elements = []
        temp = self.head
        while True:
            elements.append(temp.data)
            temp = temp.next
            if temp == self.head:  # Stop when back to head
                break

        for index, ele in enumerate(elements):
            print(f'Data {index+1}: {ele}')

    def search_ele(self, value):
        if not self.head:
            print('Circular Linked List is empty')
            return

        index = 0
        temp = self.head
        while True:
            index += 1
            if temp.data == value:
                print(f'Element found at node: {index}')
                return 
            temp = temp.next
            if temp == self.head:
                break

        print(f'Element {value} is not in the list')
        



cll = CircularLinkedList()
print('Circular Linked List: Search an element in Circular Linked List.')
print('-------------------------------------------')

n = int(input("Enter the number of nodes: "))

for i in range(n):
    value = int(input(f"Enter data for node {i+1}: "))
    cll.append(value)


print('\nData Entered in the list: ')
cll.display()

value = int(input('input the element you want to find: '))
cll.search_ele(value)


'''
OUTPUT

Circular Linked List: Search an element in Circular Linked List.
-------------------------------------------
Enter the number of nodes: 3
Enter data for node 1: 2
Enter data for node 2: 5
Enter data for node 3: 9

Data Entered in the list:
Data 1: 2
Data 2: 5
Data 3: 9
input the element you want to find: 5
Element found at node: 2

'''
