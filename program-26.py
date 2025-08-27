# Q26: Write a python in program to sort an array using selection sort.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr

arr = []
size = int(input('Enter the size of the array: '))

print('Enter elements in the array: ')
for _ in range(size):
    ele = int(input('> '))
    arr.append(ele)


print('Unsorted array\n ', arr)
print('After sorting array: \n', selection_sort(arr))

'''
OUTPUT

Enter the size of the array: 5
Enter elements in the array.
> 4
> 6
> 2
> 5
> 9
Unsorted array
  [4, 6, 2, 5, 9]
After sorting array:
 [2, 4, 5, 6, 9]

'''
