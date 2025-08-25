# Q8: Write a program to delete and display in circular queue by using array.

size = 5
queue = [10, 20, 30, 40, 50]
front = 0
rear = 4


def delete():
    global front, rear
    if front == -1:
        print("Queue is empty.")
    else:
        print(f"Deleted element: {queue[front]}")
        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % size

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
1. Dequeue
2. Display
3. Exit
''')

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        delete()
    elif choice == 2:
        display()
    elif choice == 3:
        break
    else:
        print("Wrong Choice.")


'''
# OUTPUT

1. Dequeue
2. Display
3. Exit

Enter your choice: 2
Elements:
10 20 30 40 50
Enter your choice: 1
Deleted element: 10
Enter your choice: 2
Elements:
20 30 40 50
Enter your choice: 3

'''
