'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''

print("\n*******************************************************")
print("5-2 More Conditional Tests")
print("*******************************************************")

# • Tests for equality and inequality with strings
test_string = "vmware"
if test_string == "vmware" or test_string == "microsoft":
    print("This is a virtualization provider")
else:
    print("This is not a virtualization provider")

# • Tests using the lower() method
test_string = "VMware"
if test_string.lower() == "vmware" or test_string == "microsoft":
    print("This is a virtualization provider")
else:
    print("This is not a virtualization provider")

# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
test_integer = 12
if test_integer > 6 or test_integer < 13 or test_integer == 12:
    print("This passes the integer test")
else:
    print("This does not pass the integer test")

# • Tests using the and keyword and the or keyword
test_integer = 12
if test_integer > 6 and test_integer < 13 and test_integer == 12:
    print("This passes the integer test")
else:
    print("This does not pass the integer test")

# • Test whether an item is in a list
test_numbers = [1, 2, 3, 4, 5]
for test_number in test_numbers:
    if test_number == 2:
        print("This number is in the list")
    else:
        print("This number is not in the list")

# • Test whether an item is not in a list
ingredient_list = ["salt", "pepper", "yeast", "water"]
for ingredient_item in ingredient_list:
    if ingredient_item != "pepperoni":
        print("This ingredient is not in the list")
    else:
        print("This ingredient is in the list")
