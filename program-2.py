# Q2 : Write a program to calculate factorial using recursion function in python.

def factorial(num):
    if num <= 1:
        return 1

    return num * factorial(num-1)


num = int(input('Enter the value: '))
print('Factorial is: ', factorial(num))


'''
# OUTPUT

Enter the value: 5
Factorial is:  120

'''
