# Q20: Write a program in python  to insert a node at the end of circular link list.
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


cll = CircularLinkedList()
print('Circular Linked List: Insert a node at the end of Circular Linked List.')
print('-------------------------------------------')
n = int(input("Enter the number of nodes: "))

for i in range(n):
    value = int(input(f"Enter data for node {i+1}: "))
    cll.append(value)


print('\nData Entered in the list: ')
cll.display()

data = int(input('Enter the data to be inserted: '))
cll.append(data)
print('After insertion the new list are: ')
cll.display()

'''
OUTPUT

Circular Linked List: Insert a node at the end of Circular Linked List.
-------------------------------------------
Enter the number of nodes: 3
Enter data for node 1: 2
Enter data for node 2: 5
Enter data for node 3: 8

Data Entered in the list:
Data 1: 2
Data 2: 5
Data 3: 8
Enter the data to be inserted: 9
After insertion the new list are:
Data 1: 2
Data 2: 5
Data 3: 8
Data 4: 9
'''
