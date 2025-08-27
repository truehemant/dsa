# Q23: Write a program to find out any key value used linear seacrh technique.

arr = []
size = int(input('Enter the size of the array: '))

print('Enter elements in the array. ')
for _ in range(size):
    ele = int(input('> '))
    arr.append(ele)

key = int(input('Which key to search: '))

print(f'{key} is found at {arr.index(key)+1}')

'''
OUTPUT

Enter the size of the array: 5
Enter elements in the array.
> 5
> 6
> 2
> 3
> 4
Which key to search: 2
2 is found at 3
'''
