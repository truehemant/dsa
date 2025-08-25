# Q7: Write a program to Insert and display in circular queue by using array.

size = 5
queue = [None] * size
front = -1
rear = -1

def insert(ele):
    global front, rear
    if (rear + 1) % size == front:
        print("Queue is full.")
    else:
        if front == -1:
            front = 0
        rear = (rear + 1) % size
        queue[rear] = ele


def display():
    global front, rear
    if front == -1:
        print("Queue is empty.")
    else:
        print("Elements: ")
        i = front
        while True:
            print(queue[i], end=" ")
            if i == rear:
                break
            i = (i + 1) % size
        print()

print('''
1. Enqueue
2. Display
3. Exit
''')

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ele = int(input('Enter element: '))
        insert(ele)
    elif choice == 2:
        display()
    elif choice == 3:
        break
    else:
        print("Wrong Choice.")


'''
# OUTPUT

1. Enqueue
2. Display
3. Exit

Enter your choice: 1
Enter element: 10
Enter your choice: 1
Enter element: 20
Enter your choice: 2
Elements:
10 20
Enter your choice: 3

'''
