'''
4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min()
and max() to make sure your list actually starts at one and ends at one
million. Also, use the
sum() function to see how quickly Python can add a million numbers.
'''
print("\n*******************************************************")
print("4-5  Summing a Million")
print("*******************************************************")
numbers = []
for value in range(1, 1000001):
    numbers.append(value)
    # print(value)
print(f"{min(numbers)}")
print(f"{max(numbers)}")
print(f"{sum(numbers)}")
