# Write a program to perform push operation and display array in stack by using array in python.

Max = 5
stack = []

print('''
1. push/insert
2. Display
3. Exit
      ''')

while True:
    oper = int(input('Enter your choice: '))
    if oper == 1:
        if len(stack) >= 5:
            print("Overflow.")
        else:
            ele = int(input('Enter element in stack: '))
            stack.append(ele)

    elif oper == 2:
        print(stack)

    elif oper == 3:
        break

    else:
        print('Invalid input, choose between 1, 2 and 3')

'''
# OUTPUT

1. push/insert
2. Display
3. Exit

Enter your choice:
> 1
Enter element in stack: 10
Enter your choice:
> 1
Enter element in stack: 20
Enter your choice:
> 2
[10, 20]
Enter your choice:
> 3

'''
