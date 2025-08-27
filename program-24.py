# Q24: Write a program to find out only value by the user Using binary search Technique.

def binary_search(arr, target):
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print('Element is found')
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print('Element is not found')
    return



arr = []
size = int(input('Enter the size of the array: '))

print('Enter elements in the array: ')
for _ in range(size):
    ele = int(input('> '))
    arr.append(ele)

key = int(input('Enter key to be search: '))
binary_search(arr, key)


'''
OUTPUT

Enter the size of the array: 5
Enter elements in the array:
> 6
> 5
> 3
> 2
> 8
Enter key to be search: 3
Element is found
'''

