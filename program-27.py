# Q27: Write a python program to sort an array using bubble sort technique.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        if not swapped:
            break  
    return arr


arr = []
size = int(input('Enter the size of the array: '))

print('Enter elements in the array: ')
for _ in range(size):
    ele = int(input('> '))
    arr.append(ele)


print('Unsorted array\n ', arr)
print('After sorting array: \n', bubble_sort(arr))

'''
OUTPUT

Enter the size of the array: 5
Enter elements in the array.
> 6
> 5
> 2
> 9
> 4
Unsorted array
  [6, 5, 2, 9, 4]
After sorting array:
 [2, 4, 5, 6, 9]

'''
