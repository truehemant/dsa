# Q1 : Write a program to create array, insert data and display in Python language.

# code
n = int(input("Enter the size of the array: "))
print("Enter values: ")

arr = []
for _ in range(n):
    ele = int(input("> "))
    arr.append(ele)

print("Your array is as follows: ")
print(arr)


'''
# OUTPUT

Enter the size of the array: 5
Enter values:
> 10
> 20
> 30
> 40
> 50
Your array is as follows:
[10, 20, 30, 40, 50]


'''
