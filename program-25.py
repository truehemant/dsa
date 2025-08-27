# Q25: Write a program to sort elements in an array Using insertion sort technique in python language.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key 
    return arr

arr = []
size = int(input('Enter the size of the array: '))

print('Enter elements in the array: ')
for _ in range(size):
    ele = int(input('> '))
    arr.append(ele)


print('Unsorted array\n ', arr)
print('After sorting array: \n', insertion_sort(arr))

'''
OUTPUT

Enter the size of the array: 5
Enter elements in the array:
> 6
> 2
> 3
> 5
> 1
Unsorted array
  [6, 2, 3, 5, 1]
After sorting array:
 [1, 2, 3, 5, 6]

'''
