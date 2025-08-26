# Q4: Write a program to pop and display operation in the stack by using array.

stack = [10, 20, 30, 40, 50]
def display():
    if stack:
        for ele in stack[::-1]: print(ele)

    else: print('Stack is empty')

def pop_element():
    index = len(stack)-1 
    print(f'Deleted element {stack[index]}')
    stack.pop(index)
    

print('''
1. pop/delete
2. Display
3. Exit
      ''')

while True:
    choice = int(input('Enter your choice: '))

    if choice == 1:
        if stack:
            pop_element()
        else:
            print('Underflow.')

    elif choice == 2: display()
    elif choice == 3: break
    else: print('Invalid input')


'''
# OUTPUT

1. pop/delete
2. Display
3. Exit

Enter your choice: 2
10
20
30
40
50
Enter your choice: 1
Deleted element 50

Enter your choice: 2
10
20
30
40
Enter your choice: 3

'''
