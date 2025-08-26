# Q14:  Write a program in python to delete first node of Singly Linked List.

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


    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
            
        removed = self.head.data
        self.head = self.head.next
        print(f"data of node 1 which is being deleted is : {removed}")


        


print('Linked List: Delete first node of Singly Linked List')
print('-------------------------------------------')
n = int(input("Enter the number of nodes: "))
linked_list = LinkedList()

for i in range(n):
    value = int(input(f"Enter data for node {i+1}: "))
    linked_list.append(value)

print('Data Entered in the list: ')
linked_list.display()

# deletee at begining
linked_list.delete_at_beginning()
print('Data after deletion of first node: ')
linked_list.display()


'''
OUTPUT

Linked List: Delete first node of Singly Linked List
-------------------------------------------
Enter the number of nodes: 3
Enter data for node 1: 2
Enter data for node 2: 3
Enter data for node 3: 4
Data Entered in the list:
Data = 2
Data = 3
Data = 4
data of node 1 which is being deleted is : 2
Data after deletion of first node:
Data = 3
Data = 4

'''
