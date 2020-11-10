'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think
of five simple foods, and
store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites
the tuple, and then use a for loop to print each of the items on the revised
menu.
'''
print("\n*******************************************************")
print("4-13 Buffet")
print("*******************************************************")
# A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and
# store them in a tuple.
basic_foods = ("pizza", "chicken", "fries", "ranch", "burgers")

# • Use a for loop to print each food the restaurant offers.
for food in basic_foods:
    print(food)

# Try to modify one of the items, and make sure that Python rejects the
# change.
# basic_foods.append("bacon")
# • The restaurant changes its menu, replacing two of the items with
# different foods. Add a line that rewrites
# the tuple, and then use a for loop to print each of the items on the
# revised menu.
basic_foods = ("pizza", "cheese", "fries", "ranch", "nuggets")
# • Use a for loop to print each food the restaurant offers.
print("\nMenu has changed!")
for food in basic_foods:
    print(food)
