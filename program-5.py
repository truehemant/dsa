# Q5: Write a program to Enqueue and display operation in queue using an array.

MAX = 5
queue = []

def enqueue(ele):
    if len(queue) >= MAX:
        print("Queue is Full! Cannot enqueue",ele)
    else:
        queue.append(ele)

def display():
    if queue:
        print('Elements: ')
        for ele in queue: print(ele)
    else:
        print("Queue is empty.")


print('''
1. Enqueue
2. Display
3. Exit
      ''')

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ele = int(input('Enter element: '))
        enqueue(ele)

    elif choice == 2: display() 
    elif choice == 3: break
    else: print("Wrong Choice.")



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
10
20
Enter your choice: 3

'''
