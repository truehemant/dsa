'''
Q13: Write a program in python to insert a new node at the middle of Singly Linked List.
Test Data and expected output : 

input the number of nodes (3 or more): 4
input data for node 1: 1
input data for node 2: 2
input data for node 3: 3
input data for node 4: 4

Data entered in the list are:
Data = 1
Data = 2
Data = 3
Data = 4

input data to insert in the middle of the list: 5
input the position to insert new node: 3

insertion completed successfully:

The new list are:
Data = 1
Data = 2
Data = 5
Data = 3
Data = 4

'''



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, index=None):
        new_node = Node(data)
        
        if index == 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 0

        if index is None:
            while current.next:
                current = current.next
            current.next = new_node
            return
        
        while current and count < index - 1:
            current = current.next
            count += 1

        print('Insertion completed successfully')
        
        if current is None:
            print("Index out of range, inserting at the end.")
            return self.insert(data)  
        
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f'Data = {current.data}')
            current = current.next


print('Linked List: insert a new node at the middle of the linked list: ')
print('-------------------------------------------')

nodes = int(input('input the number of nodes (3 or more): '))


linked_list = LinkedList()

for i in range(nodes):
    value = int(input(f"Enter data for node {i+1}: "))
    linked_list.insert(value)


print('Data after inserted in the list are: ')
linked_list.display()

# insert at middle
data = int(input('input data to insert in the middle of the list: '))
index = int(input('input the position to insert new node: ')) - 1
linked_list.insert(data, index)

print('The new list are: ')
linked_list.display()



'''
#OUTPUT

Linked List: insert a new node at the middle of the linked list:
-------------------------------------------
input the number of nodes (3 or more): 4
Enter data for node 1: 1
Enter data for node 2: 2
Enter data for node 3: 3
Enter data for node 4: 4
Data after inserted in the list are:
Data = 1
Data = 2
Data = 3
Data = 4
input data to insert in the middle of the list: 5
input the position to insert new node: 3
Insertion completed successfully
The new list are:
Data = 1
Data = 2
Data = 5
Data = 3
Data = 4
'''
