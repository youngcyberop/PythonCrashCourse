'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your
code should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False.'''
print("\n*******************************************************")
print("5-1 Conditional Tests")
print("*******************************************************")

# True tests

# Test 1
test1_car = 'honda'
print("is test1_car == 'Honda'? I predict true")
print(test1_car == 'honda')

# Test 2
test2_number = 1
print("does test2_number == 1? I predict true")
print(test2_number == 1)

# Test 3
test3_number = 1
print("is test3_number <= 1? I predict true")
print(test3_number <= 1)

# Test 4
test4_numbers = [1, 2, 3, 4, 5]
print("is 1 in test4_numbers? I predict true")
print(1 in test4_numbers)

# Test 5
test5_numbers = [5, 6, 7, 8]
print("is 1 not in test5_numbers? I predict true")
print(1 not in test5_numbers)

# Test 6
test6_number = 1
print("is 2 in test6_number? I predict false")
print(test6_number == 2)

# Test 7
test7_numbers = [1, 2, 3, 4, 5]
print("is 6 in test7_numbers? I predict false")
print(6 in test7_numbers)

# Test 8
test8_state = True
print("is test8_state equal to false? I predict false")
print(test8_state == False)

# Test 9
recalled_cars = ['volvo', 'lexus']
print("is honda not in recalled_cars? I predict false")
if 'honda' not in recalled_cars:
    print('False')

# Test 10
my_pizza = 'supreme'
friends_pizza = 'thin'
pizza_choice = 'thick'
print("does pizza choice == my pizza or friends_pizza? I predict false")
if my_pizza == pizza_choice or friends_pizza == pizza_choice:
    print("true - getting")
else:
    print("false - not getting")
