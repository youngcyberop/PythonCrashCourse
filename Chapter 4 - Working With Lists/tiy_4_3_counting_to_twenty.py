'''
#   Range function generates a series of numbers
#   Range starts counting at 0
#   Syntax: for value in range(1, 5):
#               print(value)
#           Read "for every value in range of numbers 1 through 5, print value
#           Output will print all numbers except for 5
#           Range output will observe the off-by-one behavior

for value in range(1, 5):
    print(value)
for value in range(0, 5):
    print(value)
for value in range(6):
    print(value)

#   Range() function can be used with list() function
#   Results can be read into a list
#       You can wrap list() round a call to the range function
#           numbers = list(range(1,6))
#           print(numbers)
numbers = list(range(1,6))
print(numbers)
#   Third argument in range function parameter tells Python to "step-size"
when generating numbers
#       Range() function starts with value 2, then adds to that value,
then does so repeatedly until
#           it reaches or passes the end value, 11
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#   squares.py
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
#   the same code can be written more concisely:
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#   min() function finds the minimum value in a list
#   max() function finds the maximum value in a list
#   sum() function finds the maximum value in a list

# example
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"{min(digits)}")
print(f"{max(digits)}")
print(f"{sum(digits)}")

#   List comprehension combines the for loop and creation of new elements
into one line
#   Syntax: list = [<expression for variable> for <variable> in <range>]
squares = [value**2 for value in range(1, 11)]
print(squares)
'''
'''
Procedure: 
    1. Begin with a descriptive name for list
    2. Open square brackets and define the expression for the values you 
    want to store in list
        - in this case, we want to raise the value to the second power
    3. Write a for loop for the numbers you want to feed into the expression
    4. Close brackets
'''
'''
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
inclusive.
'''
print("\n*******************************************************")
print("4-3 Counting to Twenty")
print("*******************************************************")
for values in range(1, 21):
    print(values)
