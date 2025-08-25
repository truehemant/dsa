# Q6: Write a program to Dequeue and display operation in queue Using an array. 

queue = [10, 20, 30, 40, 50]

def dequeue():
    if len(queue):
        removed = queue.pop(0)
        print('Deleted element ', removed)
    else:
        print('Queue is empty.')

def display():
    if queue:
        print('Elements: ')
        for ele in queue:
            print(ele)
    else:
        print("Queue is empty.")


print('''
1. Dequeue
2. Display
3. Exit
      ''')

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dequeue()

    elif choice == 2: display() 
    elif choice == 3: break
    else: print("Wrong Choice.")



'''
# OUTPUT

1. Dequeue
2. Display
3. Exit

Enter your choice: 2
Elements:
10
20
30
40
50
Enter your choice: 1
Deleted element  10
Enter your choice: 2
Elements:
20
30
40
50
Enter your choice: 3

'''
