# Q28: Write a python program to sort an array using quick sort technique.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  

    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = []
size = int(input('Enter the size of the array: '))

print('Enter elements in the array: ')
for _ in range(size):
    ele = int(input('> '))
    arr.append(ele)


print('Unsorted array\n ', arr)
print('After sorting array: \n', quick_sort(arr))

'''
OUTPUT

Enter the size of the array: 5
Enter elements in the array:
> 6
> 2
> 8
> 9
> 4
Unsorted array
  [6, 2, 8, 9, 4]
After sorting array:
  [2, 4, 6, 8, 9]

'''
